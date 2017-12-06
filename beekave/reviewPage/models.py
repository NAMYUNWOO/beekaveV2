from django.db import models
from detail.models import Movie
from django.contrib.auth.models import User


class reviewMovie(models.Model):
    reviewUser = models.ForeignKey(User,related_name="author",default=0)
    date = models.DateTimeField()
    comment = models.CharField(max_length=2000)
    score = models.FloatField()
    movieCode = models.ForeignKey(Movie,null=False)
    recommend = models.IntegerField()
    nonRecommend = models.IntegerField()
    votingUser = models.ManyToManyField(User,related_name="votingUser")
    def __str__(self):
        return self.comment[:7]