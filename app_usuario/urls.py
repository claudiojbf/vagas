from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('empresa/', views.cadastro_empresa, name='empresa'),
    path('candidato/', views.cadastro_candidato, name='candidato'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name = 'logout'),
]