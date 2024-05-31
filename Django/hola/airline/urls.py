from django.urls import path
from . import views

app_name = 'airline'

urlpatterns = [
    path("",views.index, name="index"),
    ]