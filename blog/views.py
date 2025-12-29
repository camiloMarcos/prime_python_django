from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    return HttpResponse("Conteudo do BLOG DO APP 1,  BLOG  da MaLê")
