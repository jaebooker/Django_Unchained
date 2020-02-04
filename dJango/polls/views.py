from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views import View 

def index(request):
    return HttpResponse("Good Morning, Starshine! The Earth says Hello!")

def show_the_time(request):
    now = datetime.now()
    html = "<html><body><h1>It's {} and your time is up!</h1></body></html>".format(now)
    return HttpResponse(html)

class SayHello(View):

    def get(self, request):
        html = "<html><body><h1>Good Morning, Starshine! The Earth says Hello!</h1></body></html>"
        return HttpResponse(html)
