"""Ejemplo 10: comparar la idea de buscar en list y dict."""


lista_estudiantes = [
    (205, "Ana"),
    (315, "Carlos"),
    (428, "Elena"),
    (532, "Mario"),
]

diccionario_estudiantes = {
    205: "Ana",
    315: "Carlos",
    428: "Elena",
    532: "Mario",
}

codigo_buscado = 428

print("=== Búsqueda en una lista ===")
for codigo, nombre in lista_estudiantes:
    print(f"Revisando el código {codigo}...")
    if codigo == codigo_buscado:
        print(f"Encontrado: {nombre}")
        break

print("\n=== Búsqueda en un diccionario ===")
print(f"Se consulta directamente la clave {codigo_buscado}.")
print("Encontrado:", diccionario_estudiantes.get(codigo_buscado))

print("\nLa lista puede recorrer varios elementos.")
print("El diccionario busca usando la clave.")
