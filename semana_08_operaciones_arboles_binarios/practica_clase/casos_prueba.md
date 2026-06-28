# Casos de prueba sugeridos

Ejecutar los casos en el orden indicado para que las relaciones entre nodos coincidan con la descripción.

| Paso | Operación | Entrada | Resultado esperado |
|---:|---|---:|---|
| 1 | Mostrar inorden | — | `20, 30, 40, 50, 60, 70, 80` |
| 2 | Buscar | 40 | Encontrado; ruta `50 -> 30 -> 40`. |
| 3 | Buscar | 99 | No encontrado; ruta `50 -> 70 -> 80`. |
| 4 | Insertar | 65 | Inserción correcta entre 60 y 70. |
| 5 | Insertar | 50 | Rechazado por ser duplicado. |
| 6 | Mostrar inorden | — | Incluye 65 y permanece ascendente. |
| 7 | Eliminar | 20 | Caso hoja; 20 desaparece. |
| 8 | Mostrar inorden | — | `30, 40, 50, 60, 65, 70, 80` |
| 9 | Eliminar | 60 | Caso de un hijo; 65 ocupa su posición. |
| 10 | Mostrar inorden | — | `30, 40, 50, 65, 70, 80` |
| 11 | Eliminar | 70 | Caso de dos hijos; se usa el sucesor 80. |
| 12 | Mostrar inorden | — | `30, 40, 50, 65, 80` |
| 13 | Eliminar | 999 | Se informa que no existe; el árbol no cambia. |
| 14 | Mostrar resumen | — | Conteos, altura, mínimo, máximo e inorden coherentes. |

## Validaciones adicionales

- Escribir `hola` cuando se solicite un valor: el sistema debe volver a pedir un entero.
- Insertar un número negativo: debe aceptarlo como entero válido.
- Eliminar todos los valores y consultar el resumen: debe manejar el árbol vacío.
- Insertar un valor después de vaciar el árbol: debe convertirse en la nueva raíz.

## Registro de resultados

Para cada caso anotar si la salida fue la esperada, qué nodos se visitaron y cómo se comprobó que el árbol conservó su propiedad de búsqueda.

