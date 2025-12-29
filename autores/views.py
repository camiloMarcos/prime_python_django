from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.

def autores(request):
    return HttpResponse("Quem Somos, DESCRIÇÃO DOS SÓCIOS, Letícia e Marcos")
