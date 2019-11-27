from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):

	def new(self):
		return self.order_by('-added_at')

	def popular(self):
		return self.order_by('-likes')

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="question_author", on_delete=models.SET_DEFAULT, default="",null=True)
	likes = models.ManyToManyField(User, related_name="question_like_user")

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, default="", on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="",null=True)
	