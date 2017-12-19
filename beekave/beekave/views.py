from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from beekave.forms import UserCreationForm
from detail.models import People,Movie
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class UserCreateView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'register_done.html'


def search(request,searchQuery):
    page = request.GET.get('page', 1)
    #apikey = '10ca0c0de1ff76a9a4fbb08ba91e9ae4'
    #searchPeopleurl = 'https://api.themoviedb.org/3/search/person?api_key=%s&language=en-US&include_adult=true&query=%s'
    #searchPeopleurl%(apikey,searchQuery)
    peopleResult = People.objects.filter(Q(peopleNm__icontains = searchQuery)|Q(peopleNmEn__icontains = searchQuery))
    peopleMovies = [person.moviecode.order_by('-opendate') for person in peopleResult]
    peopleResult_ = sorted(zip(peopleResult, peopleMovies),key=lambda x:len(x[1]),reverse=True)
    peopleResultCnt = peopleResult.count()
    movieResult = Movie.objects.filter(Q(title__icontains = searchQuery)|Q(titleen__icontains = searchQuery)).all()
    movieResultCnt = movieResult.count()
    paginator = Paginator(movieResult, 20)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    context = {
        "searchQuery":searchQuery,
        "movieResultCnt":movieResultCnt,
        "peopleResultCnt":peopleResultCnt,
        "peopleResult":peopleResult_,
        "movies":movies,

    }
    return render(request,"searchResult.html",context)