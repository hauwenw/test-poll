from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.QuestionView.as_view(), name='question'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='question-vote'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.QuestionResultView.as_view(), name='question-result'),
]