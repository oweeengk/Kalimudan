from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Questions

def index(request):
  latest_question_list = Questions.objects.order_by("-publication_date")[:5]
  template = loader.get_template("polls/index.html")
  context = {
     "latest_question_list": latest_question_list,
  }
  return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    

def results(request, question_id):
  response = "You're looking at the results of the question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
   return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
