"""Ejemplo 01: Nodo raiz de un arbol binario.

Este programa crea un nodo y lo usa como raiz de un arbol.
"""


class Nodo:
    """Representa un nodo dentro de un arbol binario."""

    def __init__(self, dato1: int,dato2: int,dato3: int) -> None:
        self.dato = dato1
        self.izquierdo = dato2
        self.derecho = dato3


def main() -> None:
    # Un nodo es una unidad que almacena un dato y referencias a otros nodos.
    # La raiz es el primer nodo del arbol; desde ella se llega al resto.
    raiz = Nodo(50,30,70)

    print("=== Ejemplo 1: Nodo raiz ===")
    print(f"Dato almacenado en la raiz: {raiz.dato}, {raiz.izquierdo}, {raiz.derecho}")
    print("La raiz no tiene padre porque es el inicio del arbol.")


if __name__ == "__main__":
    main()
