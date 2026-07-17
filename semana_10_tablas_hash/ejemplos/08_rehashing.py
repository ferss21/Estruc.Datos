"""Ejemplo 8: aumentar la tabla y recalcular los índices."""


def insertar(tabla, codigo, nombre):
    indice = codigo % len(tabla)
    tabla[indice].append((codigo, nombre))
    print(f"{codigo} - {nombre} -> índice {indice}")


def mostrar(tabla):
    for indice, bucket in enumerate(tabla):
        print(f"Índice {indice}: {bucket}")


estudiantes = [(205, "Ana"), (315, "Carlos"), (428, "Elena"), (532, "Mario")]

print("=== Tabla inicial: tamaño 5 ===")
tabla_inicial = [[] for _ in range(5)]
for codigo, nombre in estudiantes:
    insertar(tabla_inicial, codigo, nombre)
mostrar(tabla_inicial)

print("\n=== Rehashing: nueva tabla de tamaño 10 ===")
tabla_nueva = [[] for _ in range(10)]
for bucket in tabla_inicial:
    for codigo, nombre in bucket:
        insertar(tabla_nueva, codigo, nombre)
mostrar(tabla_nueva)
