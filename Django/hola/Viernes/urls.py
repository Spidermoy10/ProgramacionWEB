from django.urls import path
from . import views

app_name = 'viernes'

urlpatterns = [
    path('indice/<str:date>', views.indiceParam, name='indice'),
    path('indice', views.indice, name='indice')
    ]