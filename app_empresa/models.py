from django.db import models
from django.contrib.auth.models import User

class Vagas(models.Model):
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
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_vaga = models.CharField(max_length=300)
    faixa_salarial = models.CharField(
        max_length=1,
        choices=SALARIO,
    )
    requisitos = models.TextField()
    escolaridade = models.CharField(
        max_length=1,
        choices=ESCOLARIDADE,
    )