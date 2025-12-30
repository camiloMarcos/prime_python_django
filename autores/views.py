from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.

def autores(request):
    return render(request, 'autores/index.html', )
