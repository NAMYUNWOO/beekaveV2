from django.shortcuts import render
from detail.models import Movie,People
from django.http import HttpResponse
from detail.forms import movieReviewForm
from django.utils import timezone
import re,json,urllib.request
from .mediaFind import youtube_search


def detail(request,id):
    detail = Movie.objects.get(pk=id)
    form = movieReviewForm
    movieTitle = detail.title
    youtubeMovieID = youtube_search(movieTitle)
    score_list = [(detail.scoreact,"연기력"),(detail.scorestory,"스토리"),(detail.scoredirector,"감독")
                 ,(detail.scoreost,"OST"),(detail.scorevisual,"영상미"),(detail.scorefresh,"신선도")]
    peopleList = People.objects.filter(moviecode=detail)
    context = {"detail":detail,"form":form,"youtubeMovieID":youtubeMovieID,"score_list":score_list,"peopleList":peopleList}
    return render(request,'detail.html',context)

def postReview(request):
    reviewScore = request.POST.get('reviewScore', None)
    reviewText =  request.POST.get('reviewText', None)
    redirectUrl =  request.POST.get('redirectUrl', None)
    moviecode = int(redirectUrl.split("/")[1])
    form = movieReviewForm()
    post = form.save(commit=False)
    post.reviewUser = request.user
    post.date = timezone.now()
    post.nonRecommend = 0
    post.recommend = 0
    post.score = reviewScore
    post.moviecode = Movie.objects.get(pk=moviecode)
    post.comment = reviewText
    if not post.score:
        post.score = 0
    else:
        post.score = float(reviewScore)
    post.save()
    context = {'url': redirectUrl}
    return HttpResponse(json.dumps(context), content_type="application/json")

