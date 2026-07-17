"""Ejemplo 5: insertar y buscar con encadenamiento."""


tabla = [[] for _ in range(10)]


def insertar(codigo, nombre):
    indice = codigo % len(tabla)
    tabla[indice].append((codigo, nombre))
    print(f"Insertado: {codigo} - {nombre} en el índice {indice}")


def buscar(codigo):
    indice = codigo % len(tabla)
    print(f"Buscando {codigo} solamente en el bucket {indice}...")

    for codigo_guardado, nombre in tabla[indice]:
        if codigo_guardado == codigo:
            print(f"Encontrado: {nombre}")
            return nombre

    print("Estudiante no encontrado.")
    return None


print("=== Búsqueda con encadenamiento ===")
insertar(205, "Ana")
insertar(315, "Carlos")
insertar(428, "Elena")

print()
buscar(315)
buscar(999)
