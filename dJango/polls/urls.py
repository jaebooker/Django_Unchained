from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('now', views.show_the_time),
    path('hello', views.SayHello.as_view()),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/vote', views.vote, name='vote'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('api', include('api.urls'))
]
