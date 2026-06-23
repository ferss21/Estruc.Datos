"""Ejemplo 01: Nodo raiz de un arbol binario.

Este programa crea un nodo y lo usa como raiz de un arbol.
"""


class Nodo:
    """Representa un nodo dentro de un arbol binario."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


def main() -> None:
    # Un nodo es una unidad que almacena un dato y referencias a otros nodos.
    # La raiz es el primer nodo del arbol; desde ella se llega al resto.
    raiz = Nodo(50)

    print("=== Ejemplo 1: Nodo raiz ===")
    print(f"Dato almacenado en la raiz: {raiz.dato}")
    print("La raiz no tiene padre porque es el inicio del arbol.")


if __name__ == "__main__":
    main()
