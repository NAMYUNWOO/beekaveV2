from django.db import models

# Create your models here.
class Movie(models.Model):
    moviecode = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=200,null=True)
    titleen = models.CharField(max_length=200,null=True)
    thumbnail = models.URLField(null=True)
    nation = models.CharField(max_length=50,null=True)
    opendate = models.DateField(blank=False,null=True)
    showtime = models.IntegerField(default=0,null=True)
    genre = models.CharField(max_length=50,null=True)
    audit = models.CharField(max_length=50,null=True)
    director = models.CharField(max_length=100,null=True)
    score = models.FloatField(null=True)
    scoreact = models.FloatField(null=True)
    scorestory = models.FloatField(null=True)
    scoredirector = models.FloatField(null=True)
    scoreost = models.FloatField(null=True)
    scorevisual = models.FloatField(null=True)
    scorefresh = models.FloatField(null=True)
    summary = models.TextField(null=True)
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