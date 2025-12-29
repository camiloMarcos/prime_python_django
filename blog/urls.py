from django.urls import path

from blog import views as blog_views
from autores import views as autores_views

urlpatterns = [
    path('', blog_views.blog),
    path('autores', autores_views.autores),
]
