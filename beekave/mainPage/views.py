from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse
from django.db.models import F
from django.core.urlresolvers import resolve
from mainPage.models import *




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

    def getParentsVal(self,x1):
        objs = x1.objects.order_by('rank')
        obj = objs.first()
        if obj.desc =="Act":
            return objs.values("rank","movieCode",title =F("movieCode__title"),thumbnail = F("movieCode__thumbnail")
                                   ,audit=F("movieCode__audit"),score = F("movieCode__scoreAct"))
        elif obj.desc =="Story":
            return objs.values("rank","movieCode",title =F("movieCode__title"),thumbnail = F("movieCode__thumbnail")
                                   ,audit=F("movieCode__audit"),score = F("movieCode__scoreStory"))
        elif obj.desc =="Director":
            return objs.values("rank","movieCode",title =F("movieCode__title"),thumbnail = F("movieCode__thumbnail")
                                   ,audit=F("movieCode__audit"),score = F("movieCode__scoreDirector"))
        elif obj.desc =="Ost":
            return objs.values("rank","movieCode",title =F("movieCode__title"),thumbnail = F("movieCode__thumbnail")
                                   ,audit=F("movieCode__audit"),score = F("movieCode__scoreOST"))
        elif obj.desc =="Visual":
            return objs.values("rank","movieCode",title =F("movieCode__title"),thumbnail = F("movieCode__thumbnail")
                                   ,audit=F("movieCode__audit"),score = F("movieCode__scoreVisual"))
        elif obj.desc =="Fresh":
            return objs.values("rank","movieCode",title =F("movieCode__title"),thumbnail = F("movieCode__thumbnail")
                                   ,audit=F("movieCode__audit"),score = F("movieCode__scoreFresh"))
    def getContext(self):
        movieFactor = ["연기","스토리","감독","OST","영상미","신선도"]
        models = [(movieFactor[i-1], eval("Movie_rank_" + str(i))) for i in range(1, 7)]
        top10_movie_mat = list(map(lambda x: (x[0],self.getParentsVal(x[1])), models))
        context = {'top10_movie_mat': top10_movie_mat, }
        return context