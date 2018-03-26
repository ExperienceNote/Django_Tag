from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(rquest):
    return HttpResponse("<h1>Hey There!! </h1>")
