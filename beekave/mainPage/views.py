from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse
from django.db.models import F
from django.core.urlresolvers import resolve
from mainPage.models import *
from detail.models import *
from django.db.models import *
import datetime


class mainPage(View):
    def get(self,request):
        isGet = self.getRequestSearch(request)
        if isGet != None:
            return isGet
        context = self.getContext()
        return render(request,'mainPage.html',context)

    def getRequestSearch(self,request):
        if request.method == 'GET':
            search_query = request.GET.get('search_box', None)
            if search_query != None:
                return HttpResponseRedirect(reverse('search', args=[search_query]))
        return None


    def getParentsVal(self,modelList,nameList):
        dtafter = datetime.datetime.now() - datetime.timedelta(days=100)
        for scoreName, model in zip(nameList,modelList):
            targetModel = model.filter(opendate__gte = dtafter)
            modelVals = targetModel.annotate(scorefactor = F(scoreName))
            yield modelVals.order_by('-scorefactor')

    def getContext(self):
        movieFactor = ["종점","연기","스토리","감독","OST","영상미","신선도"]
        #sorted(list(movieFactor,key=lambda x: x.scoreact, reverse=True)[:10]
        scoreall = Movie.objects.filter(score__isnull=False)
        scoreact = Movie.objects.filter(Q(scoreact__isnull=False) & ~Q(genre="애니메이션"))
        scorestory = Movie.objects.filter(scorestory__isnull=False)
        scoredirector = Movie.objects.filter(scoredirector__isnull=False)
        scoreost = Movie.objects.filter(scoreost__isnull=False)
        scorevisual = Movie.objects.filter(scorevisual__isnull=False)
        scorefresh = Movie.objects.filter(scorefresh__isnull=False)
        scoreList = [scoreall,scoreact,scorestory,scoredirector,scoreost,scorevisual,scorefresh]
        nameList = ['score','scoreact','scorestory','scoredirector','scoreost','scorevisual','scorefresh']
        factorSortedList = list(self.getParentsVal(scoreList,nameList))

        top10_movie_mat = [(movieFactor[i],factorSortedList[i]) for i in range(7)]
        scoreallTop10 = top10_movie_mat[0][1]
        #thumbnail = self.gethumnails([mv['moviecode'] for mv in scoreallTop10])
        #print(thumbnail)
        context = {'top10_movie_mat': top10_movie_mat[1:], "scoreallTop10":scoreallTop10}
        return context