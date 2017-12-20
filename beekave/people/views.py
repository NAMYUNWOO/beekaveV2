from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from detail.models import Movie
from django.db.models import F
from movielist.filter import MovieFilter
from detail.models import People
import datetime
import re


def peopleFilmo(request,peopleCd):
    scoreT = ''
    scoreT_raw = 'score'
    year_ = 0
    page = request.GET.get('page', 1)
    person = People.objects.get(pk=peopleCd)
    try:
        scoreT = request.GET['score']
        year_ = request.GET['openyear']
        scoreT_raw = re.findall(r'\w+', scoreT)[0]
    except:
        pass
    filterMessage = person.peopleNm +"의 영화들"
    mvs = person.moviecode.distinct()
    if scoreT == '':
        movie_list =mvs.order_by("-opendate").annotate(scorefactor = F(scoreT_raw)).all()
    else:
        movie_list =mvs.order_by(scoreT).annotate(scorefactor = F(scoreT_raw)).all()

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
        "form":movie_filter.form,
        "movies":movies,
        "selected":scoreT,
        "filterMessage":filterMessage,
        "scoreHan":scoreHan,

    }
    return render(request,"movielist.html",context)
