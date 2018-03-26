from django.shortcuts import render
# Create your views here.

def index(rquest):
    return render(request,'app1/home.html')
