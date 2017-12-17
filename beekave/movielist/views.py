from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from detail.models import Movie
from .filter import MovieFilter
import datetime


def getword(range,scoretype,openyear = 0):

    score_word = {"-score": "총점 높은순", "-scoreact": "연기 점수 높은순", "-scorestory": "스토리 점수 높은순",
                  "-scoredirector": "감독 점수 높은순", "-scoreost": "OST 점수 높은순",
                  "-scorevisual": "영상미 점수 높은순", "-scorefresh": "신선도 점수 높은순",
                  "score": "총점 낮은순", "scoreact": "연기 점수 낮은순", "scorestory": "스토리 점수 낮은순",
                  "scoredirector": "감독 점수 낮은순", "scoreost": "OST 점수 낮은순",
                  "scorevisual": "영상미 점수 낮은순", "scorefresh": "신선도 점수 낮은순"}

    filterMessage = ""
    if openyear:
        filterMessage = str(openyear)+"년"
    else:
        if range == "alltime":
            filterMessage = "역대"
        else:
            filterMessage = "최근 6개월간"
    filterMessage = filterMessage +" "+ score_word[scoretype]
    return filterMessage


def movielist(request,range,scoretype):
    scoreT = scoretype
    year_ = 0
    page = request.GET.get('page', 1)
    try:
        scoreT = request.GET['score']
        year_ = request.GET['openyear']
    except:
        pass
    filterMessage = getword(range,scoreT,year_)
    if range == "alltime" or year_:
        movie_list = Movie.objects.order_by(scoreT).all()
    else:
        dtafter = datetime.datetime.now()-datetime.timedelta(180)
        movie_list = Movie.objects.filter(opendate__gte = dtafter).order_by(scoreT).all()

    movie_filter = MovieFilter(request.GET, queryset=movie_list)
    paginator = Paginator(movie_filter.qs, 20)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    context ={
        "range":range,
        "scoretype":scoretype,
        "form":movie_filter.form,
        "movies":movies,
        "selected":scoreT,
        "filterMessage":filterMessage,

    }
    return render(request,"movielist.html",context)
