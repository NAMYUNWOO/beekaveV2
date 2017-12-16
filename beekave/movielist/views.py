from django.shortcuts import render
from detail.models import Movie
from .filter import MovieFilter
from urllib import parse

# Create your views here.
def movielist(request,range,scoretype):
    movie_list = Movie.objects.order_by("-opendate").all()
    movie_filter = MovieFilter(request.GET, queryset=movie_list)
    context ={
        "range":range,
        "scoretype":scoretype,
        "filter":movie_filter,
    }

    return render(request,"movielist.html",context)
