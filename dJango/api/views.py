from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render

from polls.models import Question, Choice
from api.serializers import QuestionSerializer
from api.serializers import ChoiceSerializer

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # def get(self, request):
    #     questions = Question.objects.all()[:20]
    #     data = QuestionSerializer(questions, many=True).data
    #     return Response(data)

class QuestionDetail(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # def get(self, request, pk):
    #     question = get_object_or_404(Question, pk=pk)
    #     data = QuestionsSerializer(question).data
    #     return Response(data)
