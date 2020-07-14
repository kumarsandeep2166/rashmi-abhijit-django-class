from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    print(request)
    return HttpResponse('<h1>This is First application</h1><b><p>i am currently developing a python project</p>')  