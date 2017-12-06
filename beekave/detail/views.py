from django.shortcuts import render
from detail.models import Movie
from django.http import HttpResponse
from detail.forms import movieReviewForm
from django.utils import timezone
import re,json

def detail(request,id):
    detail = Movie.objects.get(pk=id)
    form = movieReviewForm
    context = {"detail":detail,"form":form,}
    return render(request,'detail.html',context)

def postReview(request):
    reviewScore = request.POST.get('reviewScore', None)
    reviewText =  request.POST.get('reviewText', None)
    redirectUrl =  request.POST.get('redirectUrl', None)
    movieCode = int(redirectUrl.split("/")[1])
    print(reviewText)
    form = movieReviewForm()
    post = form.save(commit=False)
    post.reviewUser = request.user
    post.date = timezone.now()
    post.nonRecommend = 0
    post.recommend = 0
    post.movieCode = Movie.objects.get(pk=movieCode)
    post.comment = reviewText
    post.score = str(float(reviewScore)/2)
    post.save()
    context = {'url': redirectUrl}
    return HttpResponse(json.dumps(context), content_type="application/json")

