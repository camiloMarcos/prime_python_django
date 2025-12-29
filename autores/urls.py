from django.urls import include, path
from autores.views import autores


urlpatterns = [
    path('', autores),
]
