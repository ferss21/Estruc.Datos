"""Ejemplo 02: buscar valores mostrando la ruta de comparación."""

# Una búsqueda eficiente sigue una sola rama en vez de recorrer todo el árbol.

class Nodo:
    """Guarda un valor del BST y las referencias a sus hijos."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """Árbol con inserción y búsqueda iterativa explicada."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Ubica un valor en una referencia vacía."""
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

    def buscar_con_ruta(self, valor: int) -> tuple[bool, list[int], list[str]]:
        """Retorna resultado, nodos visitados y decisiones tomadas."""
        actual = self.raiz
        ruta: list[int] = []
        decisiones: list[str] = []
        while actual is not None:
            ruta.append(actual.dato)
            if valor == actual.dato:
                decisiones.append(f"{valor} = {actual.dato}: encontrado")
                return True, ruta, decisiones
            if valor < actual.dato:
                decisiones.append(f"{valor} < {actual.dato}: ir a la izquierda")
                actual = actual.izquierdo
            else:
                decisiones.append(f"{valor} > {actual.dato}: ir a la derecha")
                actual = actual.derecho
        decisiones.append("Se llegó a una rama vacía")
        return False, ruta, decisiones


def main() -> None:
    """Busca valores existentes e inexistentes en el árbol base ampliado."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80, 65]:
        arbol.insertar(valor)

    print("=== Ejemplo 02: Búsqueda con ruta ===")
    for buscado in [40, 65, 99]:
        encontrado, ruta, decisiones = arbol.buscar_con_ruta(buscado)
        print(f"\nBuscar {buscado}")
        print("Ruta:", " -> ".join(str(valor) for valor in ruta))
        for decision in decisiones:
            print(" -", decision)
        print("Resultado:", "encontrado" if encontrado else "no encontrado")


if __name__ == "__main__":
    main()
