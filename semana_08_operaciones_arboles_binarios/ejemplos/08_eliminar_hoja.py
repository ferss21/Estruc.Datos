"""Ejemplo 08: eliminar una hoja sin afectar otras ramas."""


class Nodo:
    """Representa cada elemento enlazado del árbol."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST con eliminación recursiva para demostrar el caso hoja."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Agrega un valor si todavía no está presente."""
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
        """Elimina el valor y retorna si realmente existía."""
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
        # Una hoja tiene ambos hijos vacíos, así que se reemplaza por None.
        if nodo.izquierdo is None and nodo.derecho is None:
            return None, True
        if nodo.izquierdo is None:
            return nodo.derecho, True
        if nodo.derecho is None:
            return nodo.izquierdo, True
        sucesor = self._minimo(nodo.derecho)
        nodo.dato = sucesor.dato
        nodo.derecho, _ = self._eliminar(nodo.derecho, sucesor.dato)
        return nodo, True

    def _minimo(self, nodo: Nodo) -> Nodo:
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def inorden(self) -> list[int]:
        """Permite verificar el orden antes y después."""
        def recorrer(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            return recorrer(nodo.izquierdo) + [nodo.dato] + recorrer(nodo.derecho)

        return recorrer(self.raiz)


def main() -> None:
    """Elimina 20, que no tiene descendientes."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    print("=== Ejemplo 08: Eliminar un nodo hoja ===")
    print("Inorden antes:", arbol.inorden())
    print("El nodo 20 no tiene hijos: se reemplaza por una rama vacía.")
    print("Eliminar 20:", "correcto" if arbol.eliminar(20) else "no encontrado")
    print("Inorden después:", arbol.inorden())


if __name__ == "__main__":
    main()

