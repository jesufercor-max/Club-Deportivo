# URls_8 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`re_path(r'^usuario_por_nombre/(?P<nombre>[a-zA-Z]+)$', views.usuario_por_nombre, name='usuario_por_nombre'),`

## Vista ##
Se ha creado la vista `usuario_por_nombre`, que permite visualizar el nombre del usuario que se llame Juan en la plantilla `usuario_por_nombre`. Existen dos formas de obtener los entrenadores con sus salario y la experiencia:

### Con QuerySet (ORM de Django): ###

`usuarios = Usuario.objects.filter(nombre__icontains=nombre)`

### Con consulta SQL cruda: ###

` usuarios = (Usuario.objects.raw("SELECT * FROM app_club_usuario u "`
                                  `+ f"WHERE u.nombre LIKE '%{nombre}%';"))`

### Renderizado: ###

`return render(request, 'app_club/usuario_por_nombre.html', {'usuario_por_nombre': usuarios })`
