from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> vista 1 shinji</h1>")

def s2(request):
    html="""
        <p> vista 2 shinji</p>
       

     """
    return HttpResponse(html)
