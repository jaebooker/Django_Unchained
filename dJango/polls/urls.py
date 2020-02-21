from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('now', views.show_the_time),
    path('hello', views.SayHello.as_view()),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:question_id>', views.question_detail, name='question_detail'),
]
