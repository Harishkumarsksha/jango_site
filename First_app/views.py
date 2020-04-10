from django.shortcuts import render 
from django.http import HttpResponse


def hello_world__view(request):

    return HttpResponse('<h1> This is response from django applications<h1>')