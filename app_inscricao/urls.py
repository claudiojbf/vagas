from django.urls import path
from . import views

urlpatterns = [
    path('inscricao/<int:id>', views.inscricao, name='inscricao'),
    path('inscrito', views.inscrito, name="inscrito")
]