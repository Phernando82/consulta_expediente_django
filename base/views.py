from django.http import HttpResponse
from django.shortcuts import render
from .apps import buscar_dados


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def bot(request):
    url = 'https://sede.mjusticia.gob.es/eConsultas/inicioNacionalidad'
    nie = 'Y6848965Q'
    numero = 529063
    ano = 2021
    buscar_dados(url, nie, numero, ano)


def form_consulta(request):
    return render(request, 'base/consulta.html')
