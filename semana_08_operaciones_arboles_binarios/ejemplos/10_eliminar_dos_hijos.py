"""Ejemplo 10: eliminar un nodo con dos hijos usando su sucesor inorden."""


class Nodo:
    """Representa un nodo del árbol y sus ramas."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST que informa el sucesor utilizado durante la eliminación."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None
        self.ultimo_sucesor: int | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta un valor respetando la relación menor/mayor."""
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
        """Elimina un valor y reinicia el registro del sucesor."""
        self.ultimo_sucesor = None
        self.raiz, eliminado = self._eliminar(self.raiz, valor, True)
        return eliminado

    def _eliminar(
        self, nodo: Nodo | None, valor: int, registrar_sucesor: bool
    ) -> tuple[Nodo | None, bool]:
        if nodo is None:
            return None, False
        if valor < nodo.dato:
            nodo.izquierdo, eliminado = self._eliminar(
                nodo.izquierdo, valor, registrar_sucesor
            )
            return nodo, eliminado
        if valor > nodo.dato:
            nodo.derecho, eliminado = self._eliminar(
                nodo.derecho, valor, registrar_sucesor
            )
            return nodo, eliminado
        if nodo.izquierdo is None:
            return nodo.derecho, True
        if nodo.derecho is None:
            return nodo.izquierdo, True

        # El menor del subárbol derecho es el siguiente valor del inorden.
        sucesor = self._minimo(nodo.derecho)
        if registrar_sucesor:
            self.ultimo_sucesor = sucesor.dato
        nodo.dato = sucesor.dato
        nodo.derecho, _ = self._eliminar(nodo.derecho, sucesor.dato, False)
        return nodo, True

    def _minimo(self, nodo: Nodo) -> Nodo:
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def inorden(self) -> list[int]:
        """Comprueba que el árbol resultante conserva su orden."""
        def recorrer(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            return recorrer(nodo.izquierdo) + [nodo.dato] + recorrer(nodo.derecho)

        return recorrer(self.raiz)


def main() -> None:
    """Elimina 70, cuyos hijos son 60 y 80."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80, 75, 90]:
        arbol.insertar(valor)

    print("=== Ejemplo 10: Eliminar nodo con dos hijos ===")
    print("Inorden antes:", arbol.inorden())
    print("El nodo 70 tiene dos hijos; se busca el mínimo de su rama derecha.")
    eliminado = arbol.eliminar(70)
    print("Sucesor inorden utilizado:", arbol.ultimo_sucesor)
    print("Eliminar 70:", "correcto" if eliminado else "no encontrado")
    print("Inorden después:", arbol.inorden())


if __name__ == "__main__":
    main()

