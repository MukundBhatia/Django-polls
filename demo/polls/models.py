import datetime
# from secrets import choice
from django.utils import timezone
from django.db import models
from django.contrib import admin
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Question.objects.all() does not produce string output

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # checking if pub_date is > than one day previous date time


class Choice(models.Model):
    # foreign key proivides Many to one mapping
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey
# above link to better understand foreignkey parameters
# cascade if parent is deleted it will affect the child too in case of restrict it will restrict parent from deleting if inherited
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# It’s important to add __str__() methods to your models, not only for your
# own convenience when dealing with the interactive prompt, but also because
# objects’ representations are used throughout Django’s automatically-generated admin.


# python shell tutorial:
# https://docs.djangoproject.com/en/4.0/intro/tutorial02/
