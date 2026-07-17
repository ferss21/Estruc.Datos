"""Ejemplo 3: reconocer una colisión."""


codigos = [205, 315, 425]
tamanio_tabla = 10

print("=== Colisiones ===")
for codigo in codigos:
    indice = codigo % tamanio_tabla
    print(f"Código {codigo} -> índice {indice}")

print("\nTodos los códigos terminan en el índice 5.")
print("Esto se llama colisión: varias claves producen el mismo índice.")
