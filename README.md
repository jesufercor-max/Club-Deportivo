# URls_9 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`path('total_puntos_por_torneo/', views.total_puntos_por_torneo, name='total_puntos_torneo'),`

## Vista ##
Se ha creado la vista `total_puntos_por_torneo`, que permite visualizar el nombre del torneo así como los puntos logrado por todos los equipos en ese torneo en la plantilla `total_puntos_por_torneo`. Existen dos formas de obtener los entrenadores con sus salario y la experiencia:

### Con QuerySet (ORM de Django): ###

`torneos = Participacion.objects.values('torneo__nombre').annotate(total_puntos=Sum('puntos'))`

### Con consulta SQL cruda: ###

`torneos = (Participacion.objects.raw("SELECT t.id, t.nombre AS torneo_nombre, SUM(p.puntos) AS total_puntos "`
                                        `+ "FROM app_club_participacion p "`
                                        `+ "JOIN app_club_torneo t ON p.torneo_id = t.id "`
                                        `+ "GROUP BY t.id, t.nombre;"))`

### Renderizado: ###

`return render(request, 'app_club/total_puntos_por_torneo.html', {'total_puntos_por_torneo': torneos})`

### .annotate ###

.annotate(total_puntos=Sum('puntos')) → agrega un nuevo campo calculado total_puntos sumando todos los puntos de las participaciones de ese torneo.
