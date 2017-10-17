# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
    content = models.CharField(max_length=100)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.content


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
