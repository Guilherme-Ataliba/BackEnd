from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, default="",
                                 choices=OPCOES_CATEGORIA)
    
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)

    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Fotografia [name={self.name}]" 