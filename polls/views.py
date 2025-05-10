from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.http import HttpResponse
from django.utils import timezone

def ver_hora_actual(request):
    hora_actual = timezone.now()
    return HttpResponse(f"La hora actual es: {hora_actual}")
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Estás en la página de encuestas!")
def index(request):
    return render (request, 'student_list.html')