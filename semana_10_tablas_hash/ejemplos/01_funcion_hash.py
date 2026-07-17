"""Ejemplo 1: calcular un índice con una función hash sencilla."""


def funcion_hash(codigo, tamanio):
    return codigo % tamanio


codigos = [201, 315, 428, 532, 649]
tamanio_tabla = 10

print("=== Función hash ===")
for codigo in codigos:
    indice = funcion_hash(codigo, tamanio_tabla)
    print(f"Código {codigo} -> índice {indice}")
