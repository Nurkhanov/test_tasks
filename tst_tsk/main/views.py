from .models import Employee
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def init_view(request):
    return render(request,'main/index.html',{'employee':Employee.objects.all()})
