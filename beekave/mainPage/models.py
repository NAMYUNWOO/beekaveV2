from django.db import models
from detail.models import Movie

# scoreAct
class Movie_rank_1(models.Model):
    rank = models.IntegerField(unique=True)
    movieCode = models.ForeignKey(Movie,null=False)
    desc = models.CharField(max_length=50,default="Act")
    def __str__(self):
        return self.desc

# scoreStory
class Movie_rank_2(models.Model):
    rank = models.IntegerField(unique=True)
    movieCode = models.ForeignKey(Movie,null=False)
    desc = models.CharField(max_length=50,default="Story")
    def __str__(self):
        return self.desc

# scoreDirector
class Movie_rank_3(models.Model):
    rank = models.IntegerField(unique=True)
    movieCode = models.ForeignKey(Movie,null=False)
    desc = models.CharField(max_length=50,default="Director")
    def __str__(self):
        return self.desc

# scoreOST
class Movie_rank_4(models.Model):
    rank = models.IntegerField(unique=True)
    movieCode = models.ForeignKey(Movie,null=False)
    desc = models.CharField(max_length=50,default="Ost")
    def __str__(self):
        return self.desc


# scoreVisual
class Movie_rank_5(models.Model):
    rank = models.IntegerField(unique=True)
    movieCode = models.ForeignKey(Movie,null=False)
    desc = models.CharField(max_length=50,default="Visual")
    def __str__(self):
        return self.desc


# scoreFresh
class Movie_rank_6(models.Model):
    rank = models.IntegerField(unique=True)
    movieCode = models.ForeignKey(Movie,null=False)
    desc = models.CharField(max_length=50,default="Fresh")
    def __str__(self):
        return self.desc