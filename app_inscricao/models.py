from django.db import models
from django.contrib.auth.models import User
from app_empresa.models import Vagas

class Inscricao(models.Model):
    SALARIO = (
        ("a", "Até 1.000"),
        ("b", "De 1.000 a 2.000"),
        ("c", "De 2.000 a 3.000"),
        ("d", "Acima de 3.000"),
    )
    ESCOLARIDADE = (
        ("A", "Ensino Fundamental"),
        ("B", "Ensino médio"),
        ("C", "Tecnólogo"),
        ("D", "Ensino Superior"),
        ("E", "Pós/MBA/Mestrado"),
        ("F", "Doutorado"),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+',)
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    faixa_salarial = models.CharField(
        max_length=1,
        choices=SALARIO,
    )
    experiencia = models.TextField()
    escolaridade = models.CharField(
        max_length=1,
        choices=ESCOLARIDADE,
    )
    pontos = models.IntegerField()
