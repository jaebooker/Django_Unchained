from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.views import View
from django.template import loader

from .models import Question

def index(request):
    return HttpResponse("Good Morning, Starshine! The Earth says Hello!")

def get_question_list(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context,request))
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)

def show_the_time(request):
    now = datetime.now()
    html = "<html><body><h1>It's {} and your time is up!</h1></body></html>".format(now)
    return HttpResponse(html)

def question_detail(request, question_id):
    return HttpResponse("Details for question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You've cast your vote for %s!" % question_id)

def results(request, question_id):
    response = "The answer is... %s!"
    return HttpResponse(response % question_id)

class SayHello(View):

    def get(self, request):
        html = "<html><body><h1>Good Morning, Starshine! The Earth says Hello!</h1></body></html>"
        return HttpResponse(html)
