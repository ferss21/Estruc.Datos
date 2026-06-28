"""Ejemplo 04: contar todos los nodos antes y después de insertar."""

# El conteo se calcula desde la estructura para comprobar las modificaciones.

class Nodo:
    """Unidad que guarda un dato dentro del árbol."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST con conteo recursivo calculado desde su estructura."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta valores diferentes y conserva el orden."""
        insertado, self.raiz = self._insertar(self.raiz, valor)
        return insertado

    def _insertar(self, nodo: Nodo | None, valor: int) -> tuple[bool, Nodo]:
        if nodo is None:
            return True, Nodo(valor)
        if valor == nodo.dato:
            return False, nodo
        if valor < nodo.dato:
            insertado, nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        else:
            insertado, nodo.derecho = self._insertar(nodo.derecho, valor)
        return insertado, nodo

    def contar_nodos(self) -> int:
        """Cuenta raíz, subárbol izquierdo y subárbol derecho."""
        def contar(nodo: Nodo | None) -> int:
            if nodo is None:
                return 0
            return 1 + contar(nodo.izquierdo) + contar(nodo.derecho)

        return contar(self.raiz)


def main() -> None:
    """Comprueba que dos inserciones aumentan el total en dos."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    print("=== Ejemplo 04: Contar nodos ===")
    print("Cantidad antes de insertar:", arbol.contar_nodos())
    for valor in [65, 75]:
        print(f"Insertar {valor}:", "correcto" if arbol.insertar(valor) else "duplicado")
    print("Cantidad después de insertar dos valores:", arbol.contar_nodos())
    print("Comprobación esperada: 7 + 2 = 9 nodos")


if __name__ == "__main__":
    main()
