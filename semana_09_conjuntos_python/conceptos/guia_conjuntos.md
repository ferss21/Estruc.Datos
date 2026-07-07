# Guía de conjuntos en Python

## ¿Qué es un conjunto?

Un conjunto es una colección de elementos únicos. En Python se representa con `set`. Por ejemplo, `{101, 102, 103}` guarda tres códigos de estudiantes. Un conjunto vacío se crea con `set()`, ya que `{}` crea un diccionario vacío.

## ¿Por qué no permite duplicados?

Cada valor solo puede aparecer una vez. Si una lista contiene `[101, 102, 101]` y se convierte con `set()`, el resultado contiene `101` y `102`. Esta propiedad sirve para limpiar datos repetidos.

## Pertenencia

La pertenencia responde si un elemento forma parte de una colección. `101 in asistieron` devuelve `True` cuando el código está presente. `104 not in asistieron` comprueba el caso contrario.

## ¿Qué significa hashable?

Los elementos de un conjunto deben ser *hashable*: deben poseer un valor identificador estable mientras estén guardados. Los enteros, cadenas y tuplas de valores inmutables pueden pertenecer a un conjunto. Las listas y los diccionarios no, porque se pueden modificar.

## Diferencias entre list, set y dict

- `list`: conserva el orden de inserción y acepta duplicados. Conviene para una secuencia de actividades o calificaciones.
- `set`: guarda datos únicos y facilita pertenencia y operaciones entre grupos. Conviene para asistencia o matrículas.
- `dict`: relaciona una clave única con un valor. Conviene para asociar cada código con una nota.

## Operaciones principales

Dados `grupo_a = {101, 102, 103}` y `grupo_b = {103, 104}`:

- Unión (`grupo_a | grupo_b`): reúne los códigos sin repetirlos.
- Intersección (`grupo_a & grupo_b`): obtiene los códigos presentes en ambos.
- Diferencia (`grupo_a - grupo_b`): obtiene los códigos de A que no están en B.
- Diferencia simétrica (`grupo_a ^ grupo_b`): obtiene los códigos que están en un solo grupo.

## Subconjunto y superconjunto

Si todos los elementos de A aparecen en B, A es subconjunto de B y B es superconjunto de A. Se comprueba con `A.issubset(B)` y `B.issuperset(A)`.

## Casos de uso reales

Los conjuntos permiten quitar registros duplicados, comparar listas de matrícula, detectar estudiantes pendientes, cruzar asistencia con entregas, revisar permisos y encontrar códigos compartidos entre grupos.

Los conjuntos no deben usarse cuando la posición o la repetición de los datos sea importante. Para mostrar una salida ordenada sin cambiar el conjunto se puede usar `sorted()`.
