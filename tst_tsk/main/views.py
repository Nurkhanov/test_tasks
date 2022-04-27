import imp
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def init_view(request):
    return HttpResponse("<h1>It's my first view!!!</h1>")
