"""Reto 02: completar el caso recursivo para medir la altura."""


class Nodo:
    """Representa un dato y sus ramas descendientes."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST preparado para practicar mediciones recursivas."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta el valor en una rama disponible."""
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
        """Debe retornar la altura de la raíz medida en aristas."""
        return self._altura(self.raiz)

    def _altura(self, nodo: Nodo | None) -> int:
        if nodo is None:
            return -1

        # TODO: calcular por separado la altura izquierda y la derecha.
        # TODO: retornar 1 más la mayor de las dos alturas.
        return 0


def main() -> None:
    """Compara la salida con una altura conocida."""
    arbol = ArbolBinarioBusqueda()
    datos = [50, 30, 70, 20, 40, 60, 80, 65]
    for valor in datos:
        arbol.insertar(valor)

    print("=== Reto 02: Calcular altura ===")
    print("Datos de prueba:", datos)
    print("Convención: árbol vacío = -1 y hoja = 0.")
    print("Resultado esperado: 3")
    print("Resultado obtenido:", arbol.altura())


if __name__ == "__main__":
    main()

