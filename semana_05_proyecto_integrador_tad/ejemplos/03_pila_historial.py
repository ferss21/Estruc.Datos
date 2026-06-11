"""Ejemplo 03: Pila de historial.

Este programa muestra cómo una pila guarda acciones y las muestra desde la más
reciente hasta la más antigua. La pila usa la regla LIFO: Last In, First Out.
"""


def registrar_acciones(historial: list[str]) -> None:
    """Agrega acciones al historial usando append()."""
    historial.append("REGISTRADO 101")
    historial.append("ENCOLADO 101")
    historial.append("ATENDIDO 101")


def mostrar_acciones(historial: list[str]) -> None:
    """Muestra las acciones registradas en el orden original."""
    print("Acciones registradas:")
    for accion in historial:
        print(accion)


def mostrar_historial_reciente(historial: list[str]) -> None:
    """Muestra la pila usando pop(), desde la ultima accion registrada."""
    print("\nMostrando historial desde la acción más reciente:")
    while historial:
        print(historial.pop())


def main() -> None:
    # Este list representa el TAD Pila.
    # Con LIFO, la ultima accion agregada es la primera en salir.
    historial = []

    registrar_acciones(historial)

    print("=== Ejemplo 3: Pila de historial ===")
    mostrar_acciones(historial)
    mostrar_historial_reciente(historial)


if __name__ == "__main__":
    main()
