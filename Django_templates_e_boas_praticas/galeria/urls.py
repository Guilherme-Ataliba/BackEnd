from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path("", index, name="index"),  # When the main page gets a request call the function index
    path("imagem/", imagem, name="imagem")
]