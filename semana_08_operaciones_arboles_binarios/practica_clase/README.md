# Práctica de clase

## Consigna

Ejecutar y analizar un sistema de operaciones sobre árboles binarios de búsqueda en Python, aplicando inserción, búsqueda, recorridos, mediciones y eliminación de nodos.

## Instrucciones

1. Abrir el proyecto en Visual Studio Code.
2. Ubicar la carpeta `semana_08_operaciones_arboles_binarios`.
3. Revisar los ejemplos de la carpeta `ejemplos`.
4. Ejecutar `practica_clase/main.py` con Python.
5. Probar inserción, búsqueda, recorridos y eliminación.
6. Eliminar un nodo hoja, un nodo con un hijo y un nodo con dos hijos.
7. Tomar capturas de cada caso.
8. Explicar la salida obtenida.
9. Subir la carpeta al repositorio.
10. Entregar un PDF con evidencias y conclusión.

## Metodología

La práctica se desarrolla en clase mediante análisis de ejemplos, ejecución del programa principal y explicación de resultados. El estudiante debe demostrar que comprende cómo cambian las ramas del árbol al insertar, buscar y eliminar valores.

Antes de elegir una opción, se recomienda dibujar el árbol actual y predecir la salida. Después se contrasta la predicción con el programa. Para las eliminaciones, el recorrido inorden funciona como control: debe permanecer ascendente.

## Secuencia sugerida

1. Mostrar el resumen inicial.
2. Buscar `40` y luego `99`; comparar sus rutas.
3. Insertar `65` e intentar insertar el duplicado `50`.
4. Eliminar `20` como hoja.
5. Eliminar `60`, que tendrá a `65` como hijo único.
6. Eliminar `70` como nodo con dos hijos.
7. Mostrar inorden y resumen después de cada modificación.

## Resultado esperado

El sistema debe rechazar entradas no enteras y valores duplicados. Debe mostrar rutas de búsqueda, cuatro recorridos, altura, conteos y extremos. Las eliminaciones existentes deben reducir el total en uno y conservar el inorden ascendente; las inexistentes no deben modificar el árbol.

## Evidencia solicitada

- Captura del menú y del resumen inicial.
- Captura de una búsqueda exitosa y otra fallida con sus rutas.
- Captura de una inserción correcta y un intento duplicado.
- Captura de cada uno de los tres casos de eliminación.
- Captura del inorden posterior a cada eliminación.
- Explicación breve debajo de cada evidencia.
- Conclusión personal sobre el efecto del orden de inserción y eliminación.

## Preguntas de reflexión

1. ¿Qué permite descartar una rama durante la búsqueda?
2. ¿Por qué el inorden sirve para validar la propiedad del BST?
3. ¿Qué cambia en la estructura al eliminar una hoja?
4. ¿Qué nodo ocupa el lugar de un nodo con un hijo?
5. ¿Cómo se selecciona el sucesor inorden en el caso de dos hijos?
6. ¿Por qué dos árboles con los mismos valores pueden tener alturas distintas?

