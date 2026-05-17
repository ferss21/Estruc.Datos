# Semana 2: Diseno y analisis de algoritmos

Material practico para reforzar los conceptos iniciales de algoritmos usando Python 3.11 o superior.

## Objetivos de aprendizaje

- Reconocer la estructura entrada, proceso y salida de un algoritmo.
- Usar variables, tipos de datos y operadores en Python.
- Aplicar condicionales, ciclos y funciones.
- Medir tiempo aproximado de ejecucion.
- Contar operaciones principales dentro de un algoritmo.
- Comparar soluciones segun su eficiencia.
- Resolver un laboratorio integrador de la semana.

## Como ejecutar los ejemplos

Abre una terminal en la carpeta del repositorio y ejecuta:

```bash
cd semana_02_algoritmos
python 01_entrada_proceso_salida.py
python 02_variables_operadores.py
python 03_condicionales.py
python 04_ciclos.py
python 05_funciones.py
python 06_tiempo_ejecucion.py
python 07_conteo_operaciones.py
python 08_comparacion_busqueda.py
```

En Windows tambien puedes usar `py` si tu instalacion lo tiene configurado:

```bash
py 01_entrada_proceso_salida.py
```

## Guia de archivos

- `01_entrada_proceso_salida.py`: calcula el promedio de dos notas y separa entrada, proceso y salida.
- `02_variables_operadores.py`: muestra tipos de datos, operadores y un calculo de subtotal, impuesto y total.
- `03_condicionales.py`: clasifica una nota como Excelente, Aprobado o Reprobado.
- `04_ciclos.py`: usa `for` y `while` para sumar, contar y recorrer listas.
- `05_funciones.py`: organiza ejercicios anteriores en funciones reutilizables.
- `06_tiempo_ejecucion.py`: mide tiempos aproximados con `time.perf_counter()`.
- `07_conteo_operaciones.py`: cuenta cuantas operaciones principales se ejecutan.
- `08_comparacion_busqueda.py`: compara busquedas en lista y en conjunto (`set`).
- `laboratorio_semana2.py`: reto para completar.
- `soluciones/laboratorio_semana2_solucion.py`: solucion completa del laboratorio.
- `tests/test_laboratorio_semana2.py`: pruebas simples con `pytest`.

## Laboratorio de la semana

Completa `laboratorio_semana2.py`. El programa debe trabajar con una lista de numeros y calcular:

- Suma total.
- Cantidad de elementos positivos.
- Numero mayor.
- Promedio.
- Conteo de operaciones principales.
- Tiempo de ejecucion aproximado.

Ejecuta el laboratorio asi:

```bash
python laboratorio_semana2.py
```

Puedes revisar la solucion despues de intentarlo:

```bash
python soluciones/laboratorio_semana2_solucion.py
```

## Pruebas opcionales

Las pruebas usan `pytest`. Si no lo tienes instalado:

```bash
pip install pytest
```

Para ejecutarlas desde la carpeta `semana_02_algoritmos`:

```bash
pytest
```

Tambien puedes ejecutarlas desde la raiz del repositorio:

```bash
pytest semana_02_algoritmos/tests
```

## Evidencia sugerida para entregar en LMS

- Archivo `.py` completado.
- Captura de pantalla de la ejecucion en VS Code o terminal.
- Breve explicacion de entrada, proceso, salida y eficiencia.

## Preguntas de reflexion

- Que diferencia hay entre que un algoritmo funcione y que sea eficiente?
- Que parte del algoritmo crece cuando aumenta la cantidad de datos?
- Por que elegir una estructura de datos adecuada puede mejorar el rendimiento?
