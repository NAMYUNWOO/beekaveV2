from django.db import models


class Nation(models.Model):
    nation = models.CharField(primary_key=True,max_length=100)
    def __str__(self):
        return self.nation

class Genre(models.Model):
    genre = models.CharField(primary_key=True,max_length=100)
    def __str__(self):
        return self.genre

class OpenYear(models.Model):
    openyear = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.openyear)

class Movie(models.Model):
    moviecode = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=200,null=True)
    titleen = models.CharField(max_length=200,null=True)
    thumbnail = models.URLField(null=True)
    opendate = models.DateField(blank=False,null=True)
    openyear = models.ForeignKey(OpenYear,null=True)
    genre = models.ForeignKey(Genre, null=True)
    nation = models.ForeignKey(Nation, null=True)
    showtime = models.IntegerField(default=0,null=True)
    audit = models.CharField(max_length=50,null=True)
    director = models.CharField(max_length=100,null=True)
    score = models.IntegerField(null=True)
    scoreact = models.IntegerField(null=True)
    scorestory = models.IntegerField(null=True)
    scoredirector = models.IntegerField(null=True)
    scoreost = models.IntegerField(null=True)
    scorevisual = models.IntegerField(null=True)
    scorefresh = models.IntegerField(null=True)
    summary = models.TextField(null=True)
    def __str__(self):
        return self.title

class People(models.Model):
    peopleCd = models.IntegerField(primary_key=True)
    peopleNm = models.CharField(max_length=200)
    peopleNmEn = models.CharField(max_length=200,null=True)
    sex = models.BooleanField()
    moviecode = models.ManyToManyField(Movie, related_name="filmos")

    def __str__(self):
        return self.peopleNm
#class Media(models.Model):


