"""Ejemplo 11: comparar alturas de un árbol compacto y uno en forma de lista."""

# El orden de inserción cambia la forma aunque el conjunto de datos sea el mismo.

class Nodo:
    """Elemento del árbol con un dato y hasta dos hijos."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST cuya forma depende del orden de inserción."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta iterativamente para observar la ruta creada."""
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

    def altura(self) -> int:
        """Calcula altura en aristas; un árbol vacío mide -1."""
        def medir(nodo: Nodo | None) -> int:
            if nodo is None:
                return -1
            return 1 + max(medir(nodo.izquierdo), medir(nodo.derecho))

        return medir(self.raiz)

    def ruta_busqueda(self, valor: int) -> list[int]:
        """Devuelve las comparaciones requeridas para llegar a un valor."""
        ruta: list[int] = []
        actual = self.raiz
        while actual is not None:
            ruta.append(actual.dato)
            if valor == actual.dato:
                break
            actual = actual.izquierdo if valor < actual.dato else actual.derecho
        return ruta


def construir(valores: list[int]) -> ArbolBinarioBusqueda:
    """Crea un árbol a partir de un orden de inserción concreto."""
    arbol = ArbolBinarioBusqueda()
    for valor in valores:
        arbol.insertar(valor)
    return arbol


def main() -> None:
    """Compara siete valores iguales insertados en órdenes diferentes."""
    datos_compactos = [40, 20, 60, 10, 30, 50, 70]
    datos_ordenados = [10, 20, 30, 40, 50, 60, 70]
    compacto = construir(datos_compactos)
    desbalanceado = construir(datos_ordenados)

    print("=== Ejemplo 11: Árbol desbalanceado ===")
    print("Mismos valores, diferente orden de inserción.")
    print("Orden compacto:", datos_compactos)
    print("Altura del árbol compacto:", compacto.altura())
    print("Ruta para buscar 70:", compacto.ruta_busqueda(70))
    print("\nOrden ascendente:", datos_ordenados)
    print("Altura del árbol desbalanceado:", desbalanceado.altura())
    print("Ruta para buscar 70:", desbalanceado.ruta_busqueda(70))
    print("Conclusión: la secuencia ordenada produjo una estructura similar a una lista.")


if __name__ == "__main__":
    main()
