from django.shortcuts import render
from reviewPage.models import reviewMovie
from django.http import HttpResponse
import json,re
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.

def validOrder(filter):
    if filter == "date":
        return "-date"
    if filter == "recommend":
        return "-recommend"
    if filter == "score":
        return "-score"
    if filter == "-score":
        return "score"


def reviews(request,id,filter,page):
    query = Q()
    filter12 = filter.split("&")
    if len(filter12) == 2:
        words = re.split(r"[^A-Za-z가-힣']+", filter12[1])
        print(words)
        for word in words:
            query &= Q(comment__icontains=word)
    query &= Q(moviecode=id)
    cmmtList = reviewMovie.objects.filter(query).order_by(validOrder(filter12[0]))


    lenCmmtList = len(cmmtList)
    pageHeadIdx = (int(page)-1)*20
    pageTailIdx = pageHeadIdx+20
    if pageTailIdx > lenCmmtList:
        pageTailIdx = lenCmmtList

    return render(request,'reviewPage.html',{"reviewList":cmmtList[pageHeadIdx:pageTailIdx]})


def review_like(request):
    review_id = request.POST.get('pk', None)
    contentsType =  request.POST.get('type', None)
    if contentsType == "m":
        review = get_object_or_404(reviewMovie, pk=review_id)
        if str(request.user) == "AnonymousUser":
            context = {'like_count': review.recommend, 'message': "로그인 후 공감 버튼을 누르실 수 있습니다."}
        elif request.user not in review.votingUser.all():
            review.votingUser.add(request.user)
            review.recommend += 1
            review.save()
            context = {'like_count': review.recommend,'message':"success"}
        else:
            review.save()
            context = {'like_count': review.recommend,'message':"이미 공감 또는 비공감 버튼을 누르셨습니다."}

    return HttpResponse(json.dumps(context), content_type="application/json")


def review_dislike(request):
    review_id = request.POST.get('pk', None)
    contentsType =  request.POST.get('type', None)
    if contentsType == "m":
        review = get_object_or_404(reviewMovie, pk=review_id)
        if str(request.user) == "AnonymousUser":
            context = {'like_count': review.recommend, 'message': "로그인 후 비공감 버튼을 누르실 수 있습니다."}
        elif request.user not in review.votingUser.all():
            review.votingUser.add(request.user)
            review.nonRecommend  += 1
            review.save()
            context = {'dislike_count': review.nonRecommend,'message':"success"}
        else:
            review.save()
            context = {'dislike_count': review.nonRecommend,'message':"이미 공감 또는 비공감 버튼을 누르셨습니다."}
    return HttpResponse(json.dumps(context), content_type="application/json")
