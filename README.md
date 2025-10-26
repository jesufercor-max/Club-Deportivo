# URls_7 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`path('participaciones/torneo/<int:torneo_id>/', views.participaciones_por_torneo, name='participaciones_por_torneo'),`

## Vista ##
Se ha creado la vista `participaciones_por_torneo`, que permite visualizar el nombre de los equipos y torneos, id de la participacion y puntos cuyo id del torneo sea 1 en la plantilla `participaciones_por_torneo`. Existen dos formas de obtener los entrenadores con sus salario y la experiencia:

### Con QuerySet (ORM de Django): ###
`   participaciones = Participacion.objects.select_related('torneo', 'equipo')`
`participaciones = Participacion.objects.filter(torneo_id=torneo_id)`

### Con consulta SQL cruda: ###

`participaciones = Participacion.objects.raw("SELECT  p.id, p.puntos, p.equipo_id, p.torneo_id" `
                                               `+ "FROM app_club_participacion p "`
                                               `+ "JOIN app_club_equipo e ON p.equipo_id = e.id "`
                                               `+ "JOIN app_club_torneo t ON p.torneo_id = t.id "`
                                               `+ "WHERE t.id = {torneo_id};")`

### Renderizado: ###

`return render(request, 'app_club/participaciones_por_torneo.html', {'participaciones_por_torneo': participaciones})`
