"""Ejemplo 7: calcular e interpretar el factor de carga."""


def mostrar_factor(cantidad_elementos, tamanio_tabla):
    factor = cantidad_elementos / tamanio_tabla
    print(f"{cantidad_elementos} elementos / {tamanio_tabla} posiciones = {factor:.2f}")

    if factor < 0.5:
        print("Bajo: pocas colisiones.")
    elif factor <= 0.75:
        print("Medio: se debe vigilar.")
    else:
        print("Alto: conviene redimensionar.")


print("=== Factor de carga ===")
mostrar_factor(3, 10)
print()
mostrar_factor(6, 10)
print()
mostrar_factor(9, 10)
