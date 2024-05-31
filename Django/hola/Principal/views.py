from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaDjango(request):
    return HttpResponse("Hola Django!")

def pepe(request):
    return HttpResponse("Hola Pepe!")

def holaTu(request, nombre):
    return HttpResponse(f'Hola {nombre.capitalize()}!')

def indice(request):
    return render(request, 'Principal/index.html')

def indiceParam(request, nombre):
    return render(request, 'Principal/saludo.html', {'nombre': nombre.capitalize()})