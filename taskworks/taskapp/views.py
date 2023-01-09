from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def operations(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res1 = x + y
    res2 = x - y
    res3 = x * y
    res4 = x / y
    return render(request, "result.html", {'add': res1,'subtract':res2,'multiply':res3,'divide':res4 })


