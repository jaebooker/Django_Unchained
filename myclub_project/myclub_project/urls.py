from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('now', views.ShowTimeView.as_view()),
    path('hello', views.SayHello.as_view()),
]
