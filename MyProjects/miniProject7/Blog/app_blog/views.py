from django.shortcuts import render
# added manually
from django.http import HttpResponse   
# Create your views here.

def  home(request):
    return render(request,'app_blog/index.html', dic)

def about(request):
    return render(request,'app_blog/about.html')