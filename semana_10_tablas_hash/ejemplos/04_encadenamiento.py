"""Ejemplo 4: resolver colisiones mediante encadenamiento."""


tabla = [[] for _ in range(10)]
estudiantes = [(205, "Ana"), (315, "Carlos"), (428, "Elena"), (425, "Luis")]

print("=== Encadenamiento ===")
for codigo, nombre in estudiantes:
    indice = codigo % len(tabla)
    tabla[indice].append((codigo, nombre))
    print(f"{codigo} - {nombre} se guardó en el bucket {indice}")

print("\nTabla hash completa:")
for indice, bucket in enumerate(tabla):
    print(f"Índice {indice}: {bucket}")
