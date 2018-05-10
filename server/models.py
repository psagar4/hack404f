from django.db import models

# Create your models here.

class Movies(models.Model):
	movie_id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=200)
	genres = models.TextField()
	overview = models.TextField()
	release_date = models.DateTimeField()

class Credits(models.Model):
	credit_id = models.CharField(primary_key=True, max_length=200)
	name = models.CharField(max_length=200)
	movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)



