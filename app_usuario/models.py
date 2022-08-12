from django.db import models
from django.contrib.auth.models import User

class TipoDeUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=3)
    
    def __str__(self):
        return self.usuario.email
