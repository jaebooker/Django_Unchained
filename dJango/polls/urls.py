from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('now', views.show_the_time),
    path('hello', views.SayHello.as_view()),
    path('<int:pk>/results', views.results.as_view(), name='results'),
    path('<int:pk>/vote', views.vote, name='vote'),
    path('<int:pk>', views.question_detail, name='question_detail'),
]
