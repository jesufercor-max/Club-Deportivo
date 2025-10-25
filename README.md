### URl_1 ###
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`path('usuario/', views.mostrar_usuario, name='mostrar_usuario')`

## Vista ##
Se ha creado la vista `mostrar_usuario`, que permite visualizar todos los usuarios en la plantilla `usuario.html`. Existen dos formas de obtener los usuarios:

# Con QuerySet (ORM de Django):#

`usuarios = Usuario.objects.all()`

# Con consulta SQL cruda: #

`usuarios = Usuario.objects.raw("SELECT * FROM app_club_usuario")`

# Renderizado: #

`return render(request, 'app_club/usuario.html', {"mostrar_usuario": usuarios})`