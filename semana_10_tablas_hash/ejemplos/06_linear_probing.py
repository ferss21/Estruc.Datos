"""Ejemplo 6: resolver colisiones con linear probing."""


tabla = [None] * 10


def insertar(codigo):
    indice_inicial = codigo % len(tabla)
    indice = indice_inicial

    print(f"Código {codigo}: índice inicial {indice_inicial}")
    while tabla[indice] is not None:
        print(f"  Colisión en {indice}; se intenta la siguiente posición.")
        indice = (indice + 1) % len(tabla)

        if indice == indice_inicial:
            print("  La tabla está llena.")
            return

    tabla[indice] = codigo
    print(f"  Guardado en el índice {indice}.")


print("=== Linear probing ===")
for codigo_estudiante in [205, 315, 425, 208]:
    insertar(codigo_estudiante)

print("\nTabla final:")
for posicion, valor in enumerate(tabla):
    print(f"Índice {posicion}: {valor}")
