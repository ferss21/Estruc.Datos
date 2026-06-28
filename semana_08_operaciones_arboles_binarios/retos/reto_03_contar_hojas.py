"""Reto 03: completar el conteo de nodos que no tienen hijos."""


class Nodo:
    """Almacena un valor y hasta dos hijos."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST para practicar un recorrido recursivo de conteo."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta solamente valores nuevos."""
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

    def contar_hojas(self) -> int:
        """Inicia el conteo desde la raíz."""
        return self._contar_hojas(self.raiz)

    def _contar_hojas(self, nodo: Nodo | None) -> int:
        if nodo is None:
            return 0

        # TODO: si ambos hijos son None, retornar 1.
        # TODO: en otro caso, sumar los resultados de ambas ramas.
        return 0


def main() -> None:
    """Presenta un árbol cuyas cuatro hojas son fáciles de identificar."""
    arbol = ArbolBinarioBusqueda()
    datos = [50, 30, 70, 20, 40, 60, 80]
    for valor in datos:
        arbol.insertar(valor)

    print("=== Reto 03: Contar hojas ===")
    print("Datos de prueba:", datos)
    print("Hojas esperadas: 20, 40, 60 y 80")
    print("Cantidad esperada: 4")
    print("Cantidad obtenida:", arbol.contar_hojas())


if __name__ == "__main__":
    main()

