from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("<h1> Ejemplo app2 2 vista 1 </h1>")
