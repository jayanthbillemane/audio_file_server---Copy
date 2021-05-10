from django.db import models


# Create your models here.
class Song(models.Model):
	Name_of_the_song=models.CharField(max_length=100)
	Duration_in_number_of_seconds=models.FloatField(null=True)
	Uploaded_time=models.DateTimeField(auto_now=False, auto_now_add=False,null=False)

	def __str__(self):
		return self.Name_of_the_song		


class Podcast(models.Model):
	Name_of_the_podcast=models.CharField(max_length=100, null=False)
	Duration_in_number_of_seconds=models.FloatField(null=True)
	Uploaded_time=models.DateTimeField(auto_now=False, auto_now_add=False,null=False)
	Host=models.CharField(max_length=100)
	Participants=models.CharField(max_length=100)

	def __str__(self):
		return self.Name_of_the_podcast		

class Audiobook(models.Model):
	Name_of_the_audiobook=models.CharField(max_length=100, null=False)
	Duration_in_number_of_seconds=models.FloatField(null=True)
	Uploaded_time=models.DateTimeField(auto_now=False, auto_now_add=False,null=False)
	Author_of_the_title=models.CharField(max_length=100,null=False)
	Participants=models.CharField(max_length=100, null=False)
	Narrator=models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.Name_of_the_audiobook	