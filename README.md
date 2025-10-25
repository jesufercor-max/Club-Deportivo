# URls_3 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
` path('entrenadorSalario/', views.mostrar_entrenador_salario, name='mostrar_entrenador_salario')`

## Vista ##
Se ha creado la vista `mostrar_entrenador_salario`, que permite visualizar la id y salario de los entrenadores en la plantilla `entrenadorSalario.html`. Existen dos formas de obtener los entrenadores con sus salario:

### Con QuerySet (ORM de Django): ###

`entrenadores = Entrenador.objects.values('id', 'salario').order_by("-salario")`

### Con consulta SQL cruda: ###

`  entrenadores = (Entrenador.objects.raw ("SELECT e.id, e.salario "`
                                           `+ "FROM app_club_entrenador e "`
                                           `+ "ORDDER BY e.salario"))`

### Renderizado: ###

`return render(request, 'app_club/entrenadorSalario.html', {'mostrar_entrenador_salario': entrenadores})`

### .values ###

Se ha usado para especificar lo que queremos mostrar del modelo Entrenador, en este caso para mostrar solo el ID y el salario
`.values('id', 'salario')`