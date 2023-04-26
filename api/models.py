from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.URLField()
    order = models.IntegerField()
    
class Character(models.Model):
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    profile = models.URLField()

class Rating(models.Model):
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()