from django.db import models

# Create your models here.
class Movie(models.Model):
    movieCode = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    nation = models.CharField(max_length=50)
    opendate = models.DateField(blank=False)
    showtime = models.IntegerField(default=0)
    genre = models.CharField(max_length=50,default="")
    audit = models.CharField(max_length=50)
    score = models.FloatField()
    scoreAct = models.FloatField()
    scoreStory = models.FloatField()
    scoreDirector = models.FloatField()
    scoreOST = models.FloatField()
    scoreVisual = models.FloatField()
    scoreFresh = models.FloatField()
    summary = models.TextField(default="")
    def __str__(self):
        return self.title

class People(models.Model):
    peopleCd = models.IntegerField(primary_key=True)
    peopleNm = models.CharField(max_length=200)
    peopleNmEn = models.CharField(max_length=200)
    sex = models.BooleanField()
    repRoleNm = models.CharField(max_length=200)
    filmos = models.ManyToManyField(Movie, related_name="filmos")

    def __str__(self):
        return self.peopleNm