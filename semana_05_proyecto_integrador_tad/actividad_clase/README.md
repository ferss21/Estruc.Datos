# Actividad de Clase - Semana 5

## Consigna

Desarrollar y ejecutar un sistema básico de tickets académicos aplicando de forma integrada lista, pila, cola y diccionario.

El estudiante debe probar el programa en clase, registrar nuevos tickets, agregarlos a la cola, atenderlos, consultar tickets por código y revisar el historial de acciones.

## Instrucciones

1. Abrir el repositorio en Visual Studio Code.
2. Entrar a la carpeta `semana_05_proyecto_integrador_tad`.
3. Revisar primero los archivos de la carpeta `ejemplos`.
4. Entrar a la carpeta `actividad_clase`.
5. Ejecutar el programa:

   ```bash
   python main.py
   ```

6. Probar las opciones del menú.
7. Registrar al menos 2 tickets nuevos.
8. Agregar al menos 2 tickets a la cola.
9. Atender al menos 1 ticket.
10. Buscar un ticket existente.
11. Buscar un ticket inexistente.
12. Revisar el historial.
13. Revisar el resumen del sistema.
14. Tomar capturas de pantalla del proceso.
15. Subir el trabajo a GitHub.

## Metodología

La actividad se realiza en clase de forma práctica. El estudiante primero revisa ejemplos pequeños de cada estructura y luego trabaja el proyecto integrador.

El objetivo es demostrar que las estructuras no se usan de forma aislada, sino que pueden combinarse para resolver un problema real.

## Resultado esperado

Incluir una salida similar a esta:

```text
=== SISTEMA DE TICKETS ACADÉMICOS ===
1. Registrar ticket
2. Agregar ticket a la cola
3. Atender siguiente ticket
4. Buscar ticket por código
5. Ver historial de acciones
6. Ver resumen del sistema
7. Salir

Seleccione una opción: 2
Ingrese el código del ticket: 101
Ticket 101 agregado a la cola.

Seleccione una opción: 3
Atendiendo ticket:
Código: 101
Estudiante: Ana
Carrera: Ingeniería en Ciberseguridad
Motivo: Consulta de matrícula
Estado: Atendido

Seleccione una opción: 5
Historial de acciones:
ATENDIDO 101
ENCOLADO 101
DATOS DE PRUEBA CARGADOS

Seleccione una opción: 6
Resumen del sistema:
Tickets registrados: 3
Tickets en cola: 0
Tickets atendidos: 1
Acciones en historial: 3
```

## Evidencia de clase

El estudiante debe entregar capturas donde se observe:

- Repositorio abierto en Visual Studio Code.
- Carpeta `semana_05_proyecto_integrador_tad`.
- Archivos de ejemplos.
- Archivo `actividad_clase/main.py`.
- Ejecución del menú.
- Registro de ticket.
- Atención de ticket.
- Historial de acciones.
- Resumen del sistema.

## Entrega

Subir el proyecto trabajado a GitHub y entregar en Canvas:

- Enlace del repositorio.
- Capturas de pantalla.
- Documento PDF con explicación breve.

## Criterios de evaluación

- Ejecuta correctamente los ejemplos.
- Ejecuta correctamente la actividad de clase.
- Usa diccionario para almacenar tickets.
- Usa cola para controlar el orden de atención.
- Usa pila para guardar historial.
- Usa lista para guardar tickets atendidos.
- El menú funciona correctamente.
- El programa valida errores básicos.
- El README está completo.
- El repositorio está ordenado en GitHub.
