from django.urls import path
from . import views

urlpatterns = [
    path('', views.enviar_correo, name='index'),
]