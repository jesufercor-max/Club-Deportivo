# URls_4 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`path('participaciones/<int:puntos_participacion>' , views.mostrar_participacion, name ='mostrar_participacion'),`

## Vista ##
Se ha creado la vista `mostrar_participacion`, que permite visualizar la id y salario de los entrenadores en la plantilla `participaciones.html`. Existen dos formas de obtener los entrenadores con sus salario:

### Con QuerySet (ORM de Django): ###

`participaciones = Participacion.objects.filter(Q(puntos__gt=25) & Q(puntos__lt=30)).order_by("-puntos")`

Usamos la letra `Q` para filtrar que lo puntos obtenidos deben estar entre 26 y 29, y usamos `__gt` (mayor que) y `__lt` (menor que) para conseguir que este entre esos parametros.

### Con consulta SQL cruda: ###

`participaciones = (Participacion.objects.raw ("SELECT * FROM app_club_participacion p "`
                                                `+ "JOIN app_club_torneo t ON p.torneo_id = t.id "`
                                                `+ "JOIN app_club_equipo e ON p.equipo_id = e.id "`
                                                `+ "WHERE p.puntos > 25 AND p.puntos < 30 "`
                                                `+ "ORDER BY p.puntos DESC "))`

### Renderizado: ###

`return render(request, 'app_club/participaciones.html', {'mostrar_participacion' : participaciones})`


### Fixtures del modelo app_club.participacion ###

Se han generado datos de la tabla intermedia Participacion con el archivo `datos_fixed.json` 