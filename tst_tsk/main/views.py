from .models import Employee
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def init_view(request, str):
    print(request.path)
    employee = Employee.objects.all().order_by('-position__level')
    employee.reverse()
    return render(request,'main/index.html',{'employee':employee})
    
