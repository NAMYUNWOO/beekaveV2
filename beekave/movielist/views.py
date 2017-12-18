from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from detail.models import Movie
from django.db.models import F
from .filter import MovieFilter
import datetime
import re

def getword(range,scoretype,openyear = 0):

    score_word = {"-score": "총점이 높은 영화들", "-scoreact": "연기 점수가 높은 영화들", "-scorestory": "스토리 점수가 높은 영화들",
                  "-scoredirector": "감독 점수가 높은 영화들", "-scoreost": "OST 점수가 높은 영화들",
                  "-scorevisual": "영상미 점수가 높은 영화들", "-scorefresh": "신선도 점수가 높은 영화들",
                  "score": "총점이 낮은 영화들", "scoreact": "연기 점수가 낮은 영화들", "scorestory": "스토리 점수가 낮은 영화들",
                  "scoredirector": "감독 점수가 낮은 영화들", "scoreost": "OST 점수가 낮은 영화들",
                  "scorevisual": "영상미 점수가 낮은 영화들", "scorefresh": "신선도 점수가 낮은 영화들"}

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
    scoreT_raw = re.findall(r'\w+',scoretype)[0]
    year_ = 0
    page = request.GET.get('page', 1)
    try:
        scoreT = request.GET['score']
        year_ = request.GET['openyear']
        scoreT_raw = re.findall(r'\w+', scoreT)[0]
    except:
        pass
    filterMessage = getword(range,scoreT,year_)
    if range == "alltime" or year_:
        movie_list = Movie.objects.order_by(scoreT).\
            values("title","moviecode","thumbnail","genre","opendate","openyear",scorefactor = F(scoreT_raw)).all()
    else:
        dtafter = datetime.datetime.now()-datetime.timedelta(180)
        movie_list = Movie.objects.filter(opendate__gte = dtafter).order_by(scoreT).\
                    values("title","moviecode","thumbnail","genre","opendate","openyear",scorefactor = F(scoreT_raw)).all()

    movie_filter = MovieFilter(request.GET, queryset=movie_list)
    paginator = Paginator(movie_filter.qs, 20)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    scoreDic= {"score": "총점", "scoreact": "연기 점수", "scorestory": "스토리 점수",
                "scoredirector": "감독 점수", "scoreost": "OST 점수",
                "scorevisual": "영상미 점수", "scorefresh": "신선도 점수"}
    scoreHan = scoreDic[scoreT_raw]
    context ={
        "range":range,
        "scoretype":scoretype,
        "form":movie_filter.form,
        "movies":movies,
        "selected":scoreT,
        "filterMessage":filterMessage,
        "scoreHan":scoreHan,

    }
    return render(request,"movielist.html",context)
