from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pagInicio(request):
    return render(request, "appInventario/Inicio.html")
