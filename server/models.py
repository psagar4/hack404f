from django.db import models

import json
# Create your models here.

class Movies(models.Model):
	movie_id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=200)
	genres = models.TextField()
	overview = models.TextField()

	def __str__(self):
		d = dict()
		d['movie_id'] = self.movie_id
		d['title'] = self.title
		d['overview'] = self.overview
		d['genres'] = self.genres

		return json.dumps(d)
				

class Credits(models.Model):
	credit_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.credit_id)

	def getname(self):
		return self.name