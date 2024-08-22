from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path("", index, name="index"),  # When the main page gets a request call the function index
    path("imagem/<int:foto_id>", imagem, name="imagem"),
    path("buscar", buscar, name="buscar")
]