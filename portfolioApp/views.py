from django.shortcuts import render
from django.conf import settings
from portfolioApp.models import Proyectos

# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'title': 'Inicio'
    })

def habilidades(request):
    return render(request, 'habilidades.html', {
        'title': 'Habilidades'
    })

def proyectos(request):
    proyectos=Proyectos.objects.all()
    return render(request, 'proyectos.html', {
        'title': 'Proyectos',
        'proyectos': proyectos
    })

def recorrido(request):
    return render(request, 'recorrido.html', {
        'title': 'Recorrido'
    })
