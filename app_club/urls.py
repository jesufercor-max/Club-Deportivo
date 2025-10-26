from django.urls import path, re_path
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('usuario/', views.mostrar_usuario, name='mostrar_usuario'),
   path('entrenador/', views.mostrar_entrenador, name='mostrar_entrenador'),
   path('entrenadorSalario/', views.mostrar_entrenador_salario, name='mostrar_entrenador_salario'),
   path('participaciones/<int:puntos_participacion>' , views.mostrar_participacion, name ='mostrar_participacion'),
   re_path(r'^entrnadoresExperiencia/(?P<salario>[0-9]+)$', views.entrenadores_con_salario, name='entrenadores_con_salario'),
   path('equipos_sin_participaciones/', views.equipos_sin_participaciones, name='equipos_sin_participaciones'),
   path('participaciones/torneo/<int:torneo_id>/', views.participaciones_por_torneo, name='participaciones_por_torneo'),
   re_path(r'^usuario_por_nombre/(?P<nombre>[a-zA-Z]+)$', views.usuario_por_nombre, name='usuario_por_nombre'),
]

