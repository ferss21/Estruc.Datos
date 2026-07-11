# Casos de prueba

| Caso | Acción | Resultado esperado |
|---|---|---|
| Resumen inicial | Seleccionar opción 9 | Inscritos 101 a 106; asistentes 101, 103 y 105; entregas 101, 102 y 105 |
| Código duplicado | Agregar 101 a inscritos | Informa que ya existe y no lo duplica |
| Código no numérico | Escribir `abc` como código | Solicita nuevamente un código numérico |
| Nueva matrícula | Agregar 107 a inscritos | 107 aparece una sola vez |
| Asistencia inválida | Agregar 999 a asistencia | Informa que 999 no está inscrito |
| Asistieron y entregaron | Seleccionar opción 5 | Muestra 101 y 105 |
| Pendientes | Seleccionar opción 6 | Muestra 103, 104 y 106 |
| Ausentes | Seleccionar opción 7 | Muestra 102, 104 y 106 |
| Comparación | Grupo B: `105 106 107` | La intersección contiene 105 y 106 |
| Conjunto vacío | Eliminar todos los códigos de un registro y consultarlo | Informa que no hay datos registrados |
