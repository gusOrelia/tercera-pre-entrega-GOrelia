from django.shortcuts import render
from django.http import HttpResponse
from appInventario.models import tablCategoria

def pagInicio(request):
    return render(request, "appInventario/Inicio.html")

def pagCategoria(request):
    categorias = tablCategoria.objects.all()
    print("Categoria")
    print(categorias)
    contexto = {"categorias": categorias}
    print("Contexto")
    print(contexto)
    return render(request, "appInventario/categoriaListado.html", contexto)

def busquedaCategoria(request):
     return render(request,'appInventario/busquedaCategoria.html')

def buscar(request):
     if request.GET['categoria']:
          categoria = request.GET['categoria']
          categorias= tablCategoria.objects.filter(curso__icontains=categoria)

          return render(request,'appInventario/resultadosBusqueda.html', {"categoria":categorias})
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)