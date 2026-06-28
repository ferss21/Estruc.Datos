"""Reto 04: completar el caso de eliminación de un nodo con dos hijos."""


class Nodo:
    """Representa un dato enlazado a dos posibles subárboles."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST cuya eliminación ya resuelve cero o un hijo."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Agrega un valor sin duplicados."""
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

    def eliminar(self, valor: int) -> bool:
        """Solicita la eliminación y devuelve si se completó."""
        self.raiz, eliminado = self._eliminar(self.raiz, valor)
        return eliminado

    def _eliminar(self, nodo: Nodo | None, valor: int) -> tuple[Nodo | None, bool]:
        if nodo is None:
            return None, False
        if valor < nodo.dato:
            nodo.izquierdo, eliminado = self._eliminar(nodo.izquierdo, valor)
            return nodo, eliminado
        if valor > nodo.dato:
            nodo.derecho, eliminado = self._eliminar(nodo.derecho, valor)
            return nodo, eliminado
        if nodo.izquierdo is None:
            return nodo.derecho, True
        if nodo.derecho is None:
            return nodo.izquierdo, True

        # TODO: encontrar el sucesor con self._minimo(nodo.derecho).
        # TODO: copiar su dato y eliminarlo del subárbol derecho.
        # Mientras falte la solución, el nodo con dos hijos permanece igual.
        return nodo, False

    def _minimo(self, nodo: Nodo) -> Nodo:
        """Encuentra el extremo izquierdo desde un nodo conocido."""
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def inorden(self) -> list[int]:
        """Devuelve el control ordenado del árbol."""
        def recorrer(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            return recorrer(nodo.izquierdo) + [nodo.dato] + recorrer(nodo.derecho)

        return recorrer(self.raiz)


def main() -> None:
    """Intenta eliminar 70, un nodo con dos hijos."""
    arbol = ArbolBinarioBusqueda()
    datos = [50, 30, 70, 20, 40, 60, 80]
    for valor in datos:
        arbol.insertar(valor)

    print("=== Reto 04: Eliminar un valor ===")
    print("Datos de prueba:", datos)
    print("Inorden antes:", arbol.inorden())
    print("Resultado esperado al eliminar 70: True")
    print("Resultado obtenido:", arbol.eliminar(70))
    print("Inorden esperado: [20, 30, 40, 50, 60, 80]")
    print("Inorden obtenido:", arbol.inorden())


if __name__ == "__main__":
    main()

