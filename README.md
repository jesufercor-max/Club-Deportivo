# URls_2 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`path('entrenador/', views.mostrar_entrenador, name='mostrar_entrenador')`

## Vista ##
Se ha creado la vista `mostrar_entrenador`, que permite visualizar la id, especialidad y salario de los entrenadores, así como a que usuario (id) pertenecen en la plantilla `entrenador.html`. Existen dos formas de obtener los entrenadores con sus usarios (id):

### Con QuerySet (ORM de Django): ###

`entrenadores = Entrenador.objects.select_related('usuario').all()`

### Con consulta SQL cruda: ###

`entrenadores = (Entrenador.objects.raw ("SELECT e.id, u.id, e.especialidad, e.salario "`
                                        `+ "FROM app_club_entrenador e "`
                                        `+ "JOIN app_club_usuario u ON e.usuario_id = u.id;"))`

### Renderizado: ###

`return render(request, 'app_club/entrenador.html', {'mostrar_entrenador': entrenadores})`