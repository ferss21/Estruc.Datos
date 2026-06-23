"""Ejemplo 02: Construccion manual de un arbol binario.

Este programa crea un arbol pequeno enlazando nodos directamente.
"""


class Nodo:
    """Representa un nodo con hijo izquierdo e hijo derecho."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


def main() -> None:
    # El nodo 50 sera la raiz y tambien el padre de 30 y 70.
    raiz = Nodo(50)

    # Un hijo es un nodo conectado debajo de otro nodo.
    raiz.izquierdo = Nodo(30)
    raiz.derecho = Nodo(70)

    # El nodo 30 es padre de 20 y 40.
    raiz.izquierdo.izquierdo = Nodo(20)
    raiz.izquierdo.derecho = Nodo(40)

    # Una hoja es un nodo que no tiene hijos.
    print("=== Ejemplo 2: Arbol binario manual ===")
    print(f"Raiz: {raiz.dato}")
    print(f"Hijo izquierdo de {raiz.dato}: {raiz.izquierdo.dato}")
    print(f"Hijo derecho de {raiz.dato}: {raiz.derecho.dato}")
    print()
    print("Hojas del arbol:")
    print(f"- {raiz.izquierdo.izquierdo.dato}")
    print(f"- {raiz.izquierdo.derecho.dato}")
    print(f"- {raiz.derecho.dato}")


if __name__ == "__main__":
    main()
