from django.urls import path
from . import views

urlpatterns = [
    path('cadastrovaga', views.cadastroVaga, name="cadastrovaga"),
    path('vagasempresa', views.vagasEmpresa, name="vagasempresa"),
    path('visualizarvaga/<int:id>', views.visualizarVaga, name="visualizarvaga"),
    path('deletarvaga/<int:id>', views.deletarVaga, name="deletarvaga"),
    path('editarvaga/<int:id>', views.editarVaga, name="editarvaga"),
    path('atulaizarvaga', views.atualizarVaga, name="atualizar_vaga"),
    path('visualizar/<int:id>', views.visualizarInscritos, name="visualizar"),
    path('detalhes/<int:id>', views.detalhes_inscrito, name="detalhes_inscrito")
]