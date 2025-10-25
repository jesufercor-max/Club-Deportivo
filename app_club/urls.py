from django.urls import path
from .import views


urlpatterns = [
   path('', views.index, name='index'),
   path('usuario/', views.mostrar_usuario, name='mostrar_usuario'),
]
