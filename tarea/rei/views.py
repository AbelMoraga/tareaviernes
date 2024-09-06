from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def nombre1(request):
    return HttpResponse("<h1> aaaa con que esto se vea estoy bien </h1>")

def nombre2(request):
    html="""
    <h1> app rei rama0 por ahora</h2>
    """
    return HttpResponse(html)
    