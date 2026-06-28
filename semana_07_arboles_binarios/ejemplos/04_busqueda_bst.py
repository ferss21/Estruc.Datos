"""Ejemplo 04: Busqueda en un arbol binario de busqueda."""


class Nodo:
    """Representa un nodo de un arbol binario de busqueda."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Implementa insercion y busqueda en un BST."""

    def __init__(self) -> None:
        self.raiz = None

    def insertar(self, valor: int) -> None:
        """Inserta un valor numerico dentro del arbol."""
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo: Nodo | None, valor: int) -> Nodo:
        """Ubica el valor respetando la regla izquierda-menor, derecha-mayor."""
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.dato:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.dato:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)

        return nodo

    def buscar(self, valor: int) -> bool:
        """Retorna True si el valor existe en el arbol."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo: Nodo | None, valor: int) -> bool:
        """Busca bajando por izquierda o derecha segun el valor."""
        if nodo is None:
            return False

        if valor == nodo.dato:
            return True

        if valor < nodo.dato:
            return self._buscar_recursivo(nodo.izquierdo, valor)

        return self._buscar_recursivo(nodo.derecho, valor)


def imprimir_resultado(arbol: ArbolBinarioBusqueda, valor: int) -> None:
    """Imprime si el valor fue encontrado o no."""
    if arbol.buscar(valor):
        print(f"Valor {valor} encontrado")
    else:
        print(f"Valor {valor} no existe")


def main() -> None:
    arbol = ArbolBinarioBusqueda()
    valores = [50, 30, 70, 20, 40, 60, 80]

    for valor in valores:
        arbol.insertar(valor)

    print("=== Ejemplo 4: Busqueda en BST ===")
    imprimir_resultado(arbol, 40)
    imprimir_resultado(arbol, 80)


if __name__ == "__main__":
    main()
