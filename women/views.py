from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello Vitalik!')


def categories(request):
    return HttpResponse("<h1>Это категории</h1>")