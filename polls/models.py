from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    description_text = models.TextField(blank=True)
    imgUrl = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class SecretGroup(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
