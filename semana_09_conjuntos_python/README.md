# Semana 9 - Conjuntos en Python

## Descripción

Esta semana inicia el estudio de los conjuntos. Un conjunto permite guardar datos únicos y comprobar pertenencia de manera sencilla. Los ejemplos usan códigos de estudiantes, asistencia, cursos y entregas.

## Objetivos

- Crear conjuntos y reconocer que no almacenan duplicados.
- Consultar pertenencia con `in` y `not in`.
- Agregar y eliminar elementos.
- Aplicar unión, intersección, diferencia y diferencia simétrica.
- Identificar subconjuntos y superconjuntos.
- Elegir entre `list`, `set` y `dict` según el problema.
- Construir una versión sencilla de un conjunto usando una lista interna.

## Estructura de carpetas

- `ejemplos`: doce programas independientes con situaciones académicas.
- `practica_clase`: una práctica guiada para analizar grupos académicos.
- `evaluacion`: una tarea evaluada, su checklist y la rúbrica.

## Comandos de ejecución con Python

Ejecutar desde la carpeta `semana_09_conjuntos_python`:

```text
python ejemplos/01_crear_conjuntos.py
python ejemplos/02_pertenencia.py
python ejemplos/03_agregar_eliminar.py
python ejemplos/04_union.py
python ejemplos/05_interseccion.py
python ejemplos/06_diferencia.py
python ejemplos/07_diferencia_simetrica.py
python ejemplos/08_subconjuntos.py
python ejemplos/09_set_vs_list.py
python ejemplos/10_set_y_dict.py
python ejemplos/11_eliminar_duplicados.py
python ejemplos/12_conjunto_personalizado.py
python practica_clase/main.py
python evaluacion/tarea_evaluada.py
```

## Conceptos clave

Un `set` no repite elementos. La unión reúne datos; la intersección conserva los comunes; la diferencia obtiene los que están en un conjunto y no en otro; la diferencia simétrica encuentra los exclusivos. Para presentar resultados ordenados se usa `sorted()`, porque el conjunto no mantiene una posición fija para sus elementos.

Los conceptos se explican directamente en los ejemplos, junto con su aplicación. También se compara `list`, `set` y `dict`, y se explica que un elemento de un conjunto debe ser *hashable*, es decir, tener un identificador estable mientras está almacenado.

## Evidencia esperada

- Capturas de la ejecución de los doce ejemplos.
- Pruebas del menú de la práctica de clase.
- Resultados de las cuatro operaciones principales.
- Tarea evaluada completada y explicación de las decisiones tomadas.
- Respuestas a las preguntas de análisis.
