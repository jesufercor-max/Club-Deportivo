from django.urls import path
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('usuario/', views.mostrar_usuario, name='mostrar_usuario'),
   path('entrenador/', views.mostrar_entrenador, name='mostrar_entrenador'),
   path('entrenadorSalario/', views.mostrar_entrenador_salario, name='mostrar_entrenador_salario')
]

