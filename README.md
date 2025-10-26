# URls_6 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`path('equipos_sin_participaciones/', views.equipos_sin_participaciones, name='equipos_sin_participaciones'),`

## Vista ##
Se ha creado la vista `equipos_sin_participaciones`, que permite visualizar el nombre de los equipos cuya participación id es =NULL en la plantilla `equipos_sin_participaciones`. Existen dos formas de obtener los entrenadores con sus salario y la experiencia:

### Con QuerySet (ORM de Django): ###

`equipos = Equipo.objects.filter(participacion=None)`

### Con consulta SQL cruda: ###

`equipos = (Equipo.objects.raw("SELECT * FROM app_club_equipo e "`
                                `+ "LEFT JOIN app_club_participacion p ON p.equipo_id = e.id "`
                                `+ "WHERE p.id IS NULL;"))`

### Renderizado: ###

`return render(request, 'app_club/equipos_sin_participaciones.html', {'equipos_sin_participaciones': equipos})`

