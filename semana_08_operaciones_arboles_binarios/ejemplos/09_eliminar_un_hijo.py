"""Ejemplo 09: eliminar un nodo que posee exactamente un hijo."""

# El hijo único se reconecta con el padre del nodo que desaparece.

class Nodo:
    """Guarda un valor y enlaces a los subárboles."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST que reconecta el hijo único al eliminar su padre."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta valores únicos."""
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
        """Elimina y conserva todos los descendientes conectados."""
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
        sucesor = self._minimo(nodo.derecho)
        nodo.dato = sucesor.dato
        nodo.derecho, _ = self._eliminar(nodo.derecho, sucesor.dato)
        return nodo, True

    def _minimo(self, nodo: Nodo) -> Nodo:
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def inorden(self) -> list[int]:
        """Devuelve los valores en orden ascendente."""
        def recorrer(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            return recorrer(nodo.izquierdo) + [nodo.dato] + recorrer(nodo.derecho)

        return recorrer(self.raiz)


def main() -> None:
    """Construye 60 -> 65 para que 60 tenga un único hijo."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80, 65]:
        arbol.insertar(valor)

    print("=== Ejemplo 09: Eliminar nodo con un hijo ===")
    print("Inorden antes:", arbol.inorden())
    print("Situación: 60 tiene un único hijo derecho, 65.")
    print("Acción: 65 ocupará el lugar de 60.")
    print("Eliminar 60:", "correcto" if arbol.eliminar(60) else "no encontrado")
    print("Inorden después:", arbol.inorden())


if __name__ == "__main__":
    main()
