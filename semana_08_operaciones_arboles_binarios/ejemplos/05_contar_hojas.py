"""Ejemplo 05: identificar y contar nodos sin hijos."""

# Un nodo con un solo hijo es interno: no debe contarse como hoja.

class Nodo:
    """Contiene un dato y enlaces opcionales a izquierda y derecha."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """Árbol que puede devolver los datos almacenados en hojas."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta un dato, excepto cuando ya está presente."""
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

    def obtener_hojas(self) -> list[int]:
        """Recorre todo el árbol y reúne solamente nodos sin hijos."""
        hojas: list[int] = []

        def visitar(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            if nodo.izquierdo is None and nodo.derecho is None:
                hojas.append(nodo.dato)
                return
            visitar(nodo.izquierdo)
            visitar(nodo.derecho)

        visitar(self.raiz)
        return hojas

    def contar_hojas(self) -> int:
        """Retorna la cantidad de hojas identificadas."""
        return len(self.obtener_hojas())


def main() -> None:
    """Presenta las hojas del árbol base y su cantidad."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    print("=== Ejemplo 05: Contar hojas ===")
    print("Una hoja no tiene hijo izquierdo ni hijo derecho.")
    print("Hojas encontradas:", arbol.obtener_hojas())
    print("Cantidad de hojas:", arbol.contar_hojas())


if __name__ == "__main__":
    main()
