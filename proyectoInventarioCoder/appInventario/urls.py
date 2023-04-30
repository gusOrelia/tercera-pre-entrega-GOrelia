from django.urls import path
from appInventario import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', views.pagInicio, name='inicio'),
]
