# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.views.generic import DetailView, ListView
# from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from .models import Question, Choice


# Create your views here.
class IndexView(ListView):
    model = Question
    template_name = 'poll/index.html'
    queryset = Question.objects.filter(
        date_published__lte=datetime.datetime.now())\
        .order_by('-date_published')


class QuestionView(DetailView):
    model = Question
    template_name = 'poll/question.html'


class QuestionResultView(DetailView):
    model = Question
    template_name = 'poll/result.html'


def vote(request, pk):
    if request.method == 'POST':
        choice_id = request.POST['choice']
        voted_choice = Choice.objects.get(id=choice_id)
        voted_choice.votes += 1
        voted_choice.save()
    return redirect('question-result', pk=pk)
