"""Ejemplo 2: insertar códigos en posiciones calculadas."""


tabla = [None] * 10
codigos = [201, 312, 423, 534, 645]

print("=== Inserción por índice hash ===")
for codigo in codigos:
    indice = codigo % len(tabla)
    tabla[indice] = codigo
    print(f"Se insertó {codigo} en el índice {indice}")

print("\nTabla final:")
for indice, codigo in enumerate(tabla):
    print(f"Índice {indice}: {codigo}")
