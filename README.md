## Uso de DecimalField (no visto en clase)

En este proyecto se ha empleado el campo especial `DecimalField` de Django para almacenar datos decimales con precisión fija, por ejemplo, el salario de los entrenadores.  
Este modelo no se ha explicado en las clases, pero se incluye aquí para garantizar exactitud en cantidades que no toleran errores de redondeo, como cifras monetarias o medidas exactas.

### ¿Qué es DecimalField?

- Permite definir:
  - **max_digits**: número total máximo de dígitos permitidos, combinando los dígitos antes y después del punto decimal.
  - **decimal_places**: cantidad de decimales que se guardan después del punto.

### Ejemplo de uso

salario = models.DecimalField(max_digits=8, decimal_places=2)

Esto permite almacenar valores desde `0.00` hasta `999999.99`.

### ¿Por qué usar DecimalField?

Se utiliza `DecimalField` y no `FloatField` para evitar errores de redondeo que pueden afectar los cálculos financieros en la aplicación. Además, ofrece máxima precisión y confiabilidad en los resultados.

### Opciones adicionales

`DecimalField` también admite otras opciones habituales, como permitir nulos (`null=True`), valores por defecto (`default=valor`), y validadores para asegurar la coherencia de los datos.
