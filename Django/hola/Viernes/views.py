from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indiceParam(request, date):
    return render(request, 'Viernes/Dia.html', {'date': date.capitalize()})

def indice(request):
    return render(request, 'Viernes/Negacion.html')
    