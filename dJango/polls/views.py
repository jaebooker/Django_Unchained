from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.template import loader
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date_lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     return HttpResponse("Good Morning, Starshine! The Earth says Hello!")
#
# def get_question_list(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     #output = ', '.join([q.question_text for q in latest_question_list])
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context,request))
#     context = {'latest_question_list': latest_question_list}
#     return render(request,'polls/index.html',context)

def show_the_time(request):
    now = datetime.now()
    html = "<html><body><h1>It's {} and your time is up!</h1></body></html>".format(now)
    return HttpResponse(html)

# def question_detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("I'm sorry to say that the question you are searching for does not exist.")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a correct choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})
#     # response = "The answer is... %s!"
#     # return HttpResponse(response % question_id)

class SayHello(View):

    def get(self, request):
        html = "<html><body><h1>Good Morning, Starshine! The Earth says Hello!</h1></body></html>"
        return HttpResponse(html)
