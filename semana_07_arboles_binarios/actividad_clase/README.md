# Actividad de Clase - Semana 7

## Consigna
Desarrollar y ejecutar un programa por consola llamado **Sistema de Arbol Binario de Codigos Academicos**. El sistema debe organizar codigos numericos de estudiantes usando un arbol binario de busqueda.

## Como ejecutar
1. Abrir el repositorio en Visual Studio Code.
2. Entrar a la carpeta `semana_07_arboles_binarios`.
3. Ejecutar los ejemplos de la carpeta `ejemplos`.
4. Ejecutar la actividad:

```bash
python3 actividad_clase/main.py
```

## Conceptos importantes

### Raiz
La raiz es el primer nodo del arbol. En este programa, la raiz inicial es el codigo `50`.

### Hoja
Una hoja es un nodo que no tiene hijos. En el arbol de prueba, `20`, `40`, `60` y `80` son hojas.

### Recorrido inorden
El recorrido inorden visita primero el subarbol izquierdo, luego la raiz y despues el subarbol derecho. En un arbol binario de busqueda, este recorrido muestra los codigos ordenados de menor a mayor.

### Utilidad del arbol binario de busqueda
El arbol binario de busqueda ayuda a organizar datos porque separa los valores menores hacia la izquierda y los valores mayores hacia la derecha. Esto facilita insertar, buscar y recorrer datos de forma ordenada.

## Prueba de ejecucion

```text
=== Sistema de Arbol Binario de Codigos Academicos ===
1. Insertar codigo
2. Buscar codigo
3. Ver recorrido preorden
4. Ver recorrido inorden
5. Ver recorrido postorden
6. Ver altura del arbol
7. Contar hojas
8. Ver resumen
9. Salir

Recorrido inorden:
20, 30, 40, 50, 60, 70, 80

Buscar 40:
Codigo 40 encontrado.

Resumen:
Raiz: 50
Cantidad de nodos: 7
Cantidad de hojas: 4
Altura: 3
```

## Capturas para entregar
El estudiante debe tomar capturas donde se observe:
- Carpeta `semana_07_arboles_binarios` en VS Code.
- Ejecucion de los ejemplos.
- Ejecucion del menu principal.
- Insercion de un codigo nuevo.
- Busqueda de un codigo existente.
- Busqueda de un codigo inexistente.
- Recorrido inorden.
- Resumen del arbol.

## Entrega esperada
- Carpeta `semana_07_arboles_binarios` subida a GitHub.
- Capturas de ejecucion.
- README completo.
- Conclusion breve explicando que aprendio sobre arboles binarios.
