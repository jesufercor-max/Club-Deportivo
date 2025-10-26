# URls_5 #
Se ha añadido la siguiente ruta en urls.py de la app_club, que apunta a la vista para mostrar a los usuarios:
`re_path(r'^entrnadoresExperiencia/(?P<salario>[0-9]+)$', views.entrenadores_con_salario, name='entrenadores_con_salario')`

## Vista ##
Se ha creado la vista `entrenadores_con_salario`, que permite visualizar la id, el salario y la experiencia de los entrenadores en la plantilla `entrnadoresExperiencia`. Existen dos formas de obtener los entrenadores con sus salario y la experiencia:

### Con QuerySet (ORM de Django): ###

`entrenadores = Entrenador.objects.filter(Q(salario__gt=salario) | Q(experiencia_anios__gt=5))`

Usamos la letra `Q`  y el `__gt`para filtrar que el salrio debe ser mayor que 2000 (pasado en la url del index.html) y que la experiencia debe ser mayor que 5 años 

### Con consulta SQL cruda: ###

`entrenadores = (Entrenador.objects.raw("SELECT e.id, e.salario, e.experiencia_anios "`
                                        `+ "FROM app_club_entrenador e "`
                                        `+ "WHERE e.salario > 2000 OR e.experiencia_anios > 5 "))`

### Renderizado: ###

`return render(request, 'app_club/entrenadoresExperiencia.html', {'entrenadores_con_salario': entrenadores})`

### re_path ###

`re_path(r'^entrnadoresExperiencia/(?P<salario>[0-9]+)$', views.entrenadores_con_salario, name='entrenadores_con_salario')`

Uso del re_path:

- ^ → indica inicio de la URL  

- entrnadoresExperiencia/ → es el literal que debe aparecer en la URL (nota: parece que hay un typo, debería ser entrenadoresExperiencia/)

- (?P<salario>[0-9]+) → grupo con nombre salario:

- [0-9]+ → uno o más dígitos

- (?P<salario>...) → Django captura esto como parámetro de la vista llamado salario

- $ → indica fin de la URL