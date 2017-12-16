from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse
from django.db.models import F
from django.core.urlresolvers import resolve
from mainPage.models import *
from detail.models import *
from django.db.models import *



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
        for scoreName, model in zip(nameList,modelList):
            targetModel = model.values("moviecode","title","thumbnail","audit",'genre',"opendate",scorefactor = F(scoreName))
            yield sorted(list(targetModel[:50]),key=lambda x:x['scorefactor'],reverse=True)[:10]
    def getContext(self):
        movieFactor = ["종점","연기","스토리","감독","OST","영상미","신선도"]
        #sorted(list(movieFactor,key=lambda x: x.scoreact, reverse=True)[:10]
        scoreall = Movie.objects.filter(score__isnull=False).order_by("-opendate")
        scoreact = Movie.objects.filter(Q(scoreact__isnull=False) & ~Q(genre="애니메이션")).order_by("-opendate")
        scorestory = Movie.objects.filter(scorestory__isnull=False).order_by("-opendate")
        scoredirector = Movie.objects.filter(scoredirector__isnull=False).order_by("-opendate")
        scoreost = Movie.objects.filter(scoreost__isnull=False).order_by("-opendate")
        scorevisual = Movie.objects.filter(scorevisual__isnull=False).order_by("-opendate")
        scorefresh = Movie.objects.filter(scorefresh__isnull=False).order_by("-opendate")
        scoreList = [scoreall,scoreact,scorestory,scoredirector,scoreost,scorevisual,scorefresh]
        nameList = ['score','scoreact','scorestory','scoredirector','scoreost','scorevisual','scorefresh']
        factorSortedList = list(self.getParentsVal(scoreList,nameList))

        top10_movie_mat = [(movieFactor[i],factorSortedList[i]) for i in range(7)]
        scoreallTop10 = top10_movie_mat[0][1][:4]
        context = {'top10_movie_mat': top10_movie_mat[1:], "scoreallTop10":scoreallTop10}
        return context