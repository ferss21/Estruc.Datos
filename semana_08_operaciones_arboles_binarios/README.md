# Semana 8 - Operaciones avanzadas en árboles binarios

## Descripción

Esta semana profundiza en las operaciones de un árbol binario de búsqueda (BST) usando Python. El trabajo se concentra en observar cómo cada comparación decide una rama y cómo las operaciones conservan el orden del árbol.

## Objetivos

- Insertar valores en un árbol binario de búsqueda.
- Buscar valores mostrando la ruta de comparación.
- Calcular altura, profundidad, cantidad de nodos y hojas.
- Mostrar el valor mínimo y el máximo.
- Ejecutar recorridos preorden, inorden, postorden y por niveles.
- Eliminar nodos en tres casos: hoja, un hijo y dos hijos.
- Interpretar las salidas y documentar evidencias.

## Relación con Semana 7

La Semana 7 presentó la estructura básica: nodo, raíz, hijos, hojas, niveles y recorridos. La Semana 8 usa esa base para resolver operaciones completas sobre un BST, analizar su costo y comprobar que el orden se mantiene después de modificarlo.

## Convención de altura y profundidad

En este material ambas medidas se cuentan en aristas. Una hoja tiene altura `0`, la raíz tiene profundidad `0` y un árbol vacío tiene altura `-1`. Indicar la convención evita respuestas ambiguas.

## Estructura de carpetas

- `conceptos`: guía de estudio y vocabulario de consulta.
- `ejemplos`: doce programas independientes con salidas listas para analizar.
- `practica_clase`: sistema de consola, instrucciones, pruebas y preguntas.
- `retos`: ejercicios con secciones `TODO` para completar.
- `evaluacion`: checklist de entrega y rúbrica.

## Comandos de ejecución con Python

Ejecutar desde la carpeta `semana_08_operaciones_arboles_binarios`:

```text
python ejemplos/01_insertar_paso_a_paso.py
python ejemplos/02_buscar_con_ruta.py
python ejemplos/03_altura_profundidad.py
python ejemplos/04_contar_nodos.py
python ejemplos/05_contar_hojas.py
python ejemplos/06_recorrido_por_niveles.py
python ejemplos/07_minimo_maximo.py
python ejemplos/08_eliminar_hoja.py
python ejemplos/09_eliminar_un_hijo.py
python ejemplos/10_eliminar_dos_hijos.py
python ejemplos/11_arbol_desbalanceado.py
python ejemplos/12_imprimir_arbol_ascii.py
python practica_clase/main.py
```

## Ruta sugerida de estudio

1. Leer la guía y consultar el vocabulario.
2. Ejecutar los ejemplos en orden y predecir cada salida.
3. Usar el sistema de práctica para modificar el árbol.
4. Registrar el inorden antes y después de cada eliminación.
5. Completar los retos y comparar el resultado con lo esperado.
6. Preparar las evidencias usando el checklist y la rúbrica.

