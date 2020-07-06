from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.registro, name="registro"),
    path('', views.estadistica, name='estadistica'),
    path('formulario', views.formulario),
]
