"""Ejemplo 03: calcular altura del árbol y profundidad de valores."""


class Nodo:
    """Representa un nodo que puede tener dos descendientes directos."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST capaz de medir altura y profundidad en aristas."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta un valor mediante llamadas recursivas."""
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

    def altura(self) -> int:
        """Retorna la ruta más larga de la raíz a una hoja, en aristas."""
        return self._altura(self.raiz)

    def _altura(self, nodo: Nodo | None) -> int:
        # El -1 permite que una hoja resulte en altura 0.
        if nodo is None:
            return -1
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    def profundidad(self, valor: int) -> int | None:
        """Retorna la distancia desde la raíz o None si el valor no existe."""
        actual = self.raiz
        profundidad_actual = 0
        while actual is not None:
            if valor == actual.dato:
                return profundidad_actual
            actual = actual.izquierdo if valor < actual.dato else actual.derecho
            profundidad_actual += 1
        return None


def main() -> None:
    """Muestra medidas con una convención explícita."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    print("=== Ejemplo 03: Altura y profundidad ===")
    print("Convención: se cuentan aristas; la raíz tiene profundidad 0.")
    print("Altura total del árbol:", arbol.altura())
    for valor in [20, 40, 80, 99]:
        profundidad = arbol.profundidad(valor)
        if profundidad is None:
            print(f"Profundidad de {valor}: no existe en el árbol")
        else:
            print(f"Profundidad de {valor}: {profundidad}")


if __name__ == "__main__":
    main()

