from django.shortcuts import render
from django.http import HttpResponse


context = {}
def home(request):
    return render(request,"page/index.html",context)
