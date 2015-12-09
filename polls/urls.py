from django.shortcuts import render

# Create your views here.

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('polls.views',
url(r'^polls', 'polls.views.index', name='index'),
)
