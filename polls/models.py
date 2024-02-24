from django.db import models
from django.contrib.auth.models import User

from django.core import serializers
import json


def jsonify(input):
    querySetString = serializers.serialize("json", input)
    jsonData = json.loads(querySetString)
    return jsonData


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def list():
        return jsonify(Question.objects.all().order_by("-pub_date"))

    def get(id):
        return Question.objects.query(pk=id)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def list():
        return jsonify(Choice.objects.all())


class SecretGroup(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
