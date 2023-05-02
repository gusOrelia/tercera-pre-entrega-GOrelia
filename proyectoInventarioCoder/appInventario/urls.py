from django.urls import path
from appInventario import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', views.pagInicio, name='inicio'),
    path('categorias', views.pagCategoria, name='categorias'),
    path('categoriasList', views.busquedaCategoria, name='categoriasList'),
    path('buscar',views.buscar),
]
