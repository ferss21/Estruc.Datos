"""Ejemplo 02: TAD Pila en Python.

Este programa simula un historial de acciones. La pila usa la regla LIFO:
Last In, First Out. Es decir, la ultima accion agregada es la primera en salir.
"""


def apilar_accion(pila: list[str], accion: str) -> None:
    """Agrega una accion en la parte superior de la pila."""
    pila.append(accion)


def desapilar_accion(pila: list[str]) -> str | None:
    """Quita y devuelve la ultima accion registrada."""
    if not pila:
        return None

    return pila.pop()


def ver_ultima_accion(pila: list[str]) -> str | None:
    """Devuelve la ultima accion sin eliminarla."""
    if not pila:
        return None

    return pila[-1]


def mostrar_pila(pila: list[str]) -> None:
    """Muestra todas las acciones de la pila."""
    if not pila:
        print("La pila esta vacia.")
        return

    print("Base -> Tope")
    for accion in pila:
        print(f"- {accion}")


def main() -> None:
    # Este list representa el TAD Pila.
    historial = ["Abrir archivo", "Editar titulo", "Guardar cambios"]

    print("=== TAD PILA ===")
    print("Datos iniciales:")
    mostrar_pila(historial)

    print("\nApilar accion: Agregar imagen")
    apilar_accion(historial, "Agregar imagen")
    mostrar_pila(historial)

    print("\nVer ultima accion")
    print(f"Ultima accion: {ver_ultima_accion(historial)}")

    print("\nDesapilar ultima accion")
    accion = desapilar_accion(historial)
    print(f"Accion retirada: {accion}")
    mostrar_pila(historial)

    print("\nConclusion: la pila atiende primero lo ultimo que se agrego.")


if __name__ == "__main__":
    main()
