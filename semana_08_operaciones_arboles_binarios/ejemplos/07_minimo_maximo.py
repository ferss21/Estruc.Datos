"""Ejemplo 07: encontrar los extremos izquierdo y derecho de un BST."""

# La propiedad del BST permite hallar los extremos sin visitar todos los nodos.

class Nodo:
    """Almacena un dato y dos referencias opcionales."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST con operaciones para consultar mínimo y máximo."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta de manera iterativa sin aceptar duplicados."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True
        actual = self.raiz
        while True:
            if valor == actual.dato:
                return False
            if valor < actual.dato:
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(valor)
                    return True
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    return True
                actual = actual.derecho

    def minimo_con_ruta(self) -> tuple[int | None, list[int]]:
        """Avanza siempre a la izquierda hasta encontrar el mínimo."""
        actual = self.raiz
        ruta: list[int] = []
        while actual is not None:
            ruta.append(actual.dato)
            if actual.izquierdo is None:
                return actual.dato, ruta
            actual = actual.izquierdo
        return None, ruta

    def maximo_con_ruta(self) -> tuple[int | None, list[int]]:
        """Avanza siempre a la derecha hasta encontrar el máximo."""
        actual = self.raiz
        ruta: list[int] = []
        while actual is not None:
            ruta.append(actual.dato)
            if actual.derecho is None:
                return actual.dato, ruta
            actual = actual.derecho
        return None, ruta


def main() -> None:
    """Muestra los valores extremos y las rutas utilizadas."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    minimo, ruta_minimo = arbol.minimo_con_ruta()
    maximo, ruta_maximo = arbol.maximo_con_ruta()
    print("=== Ejemplo 07: Mínimo y máximo ===")
    print("El mínimo está en el extremo izquierdo.")
    print("Ruta al mínimo:", " -> ".join(map(str, ruta_minimo)), "| mínimo:", minimo)
    print("El máximo está en el extremo derecho.")
    print("Ruta al máximo:", " -> ".join(map(str, ruta_maximo)), "| máximo:", maximo)


if __name__ == "__main__":
    main()
