"""Ejemplo 01: insertar un valor y explicar cada comparación."""

# La ruta permite relacionar cada comparación con una rama del árbol.

class Nodo:
    """Representa un dato y sus dos posibles ramas."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """Inserta valores sin duplicados y puede informar la ruta seguida."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta sin mostrar detalles; retorna False si el valor ya existe."""
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

    def insertar_con_ruta(self, valor: int) -> tuple[bool, list[str]]:
        """Inserta iterativamente y guarda las decisiones como evidencia."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True, [f"{valor} se convierte en la raíz"]

        ruta: list[str] = []
        actual = self.raiz
        while True:
            if valor == actual.dato:
                ruta.append(f"{valor} ya existe")
                return False, ruta
            if valor < actual.dato:
                ruta.append(f"{actual.dato} -> izquierda")
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(valor)
                    return True, ruta
                actual = actual.izquierdo
            else:
                ruta.append(f"{actual.dato} -> derecha")
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    return True, ruta
                actual = actual.derecho

    def inorden(self) -> list[int]:
        """Devuelve los valores ordenados para comprobar la inserción."""
        def recorrer(nodo: Nodo | None) -> list[int]:
            if nodo is None:
                return []
            return recorrer(nodo.izquierdo) + [nodo.dato] + recorrer(nodo.derecho)

        return recorrer(self.raiz)


def main() -> None:
    """Carga el árbol base e inserta 65 paso a paso."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    print("=== Ejemplo 01: Inserción paso a paso ===")
    print("Árbol inicial (inorden):", arbol.inorden())
    insertado, ruta = arbol.insertar_con_ruta(65)
    print("Valor a insertar: 65")
    print("Comparaciones realizadas:")
    for paso in ruta:
        print(" -", paso)
    nodos_visitados = [paso.split(" -> ")[0] for paso in ruta]
    direccion_final = ruta[-1].split(" -> ")[-1]
    print("Ruta de inserción:", " -> ".join(nodos_visitados + [direccion_final]))
    print("Resultado:", "65 insertado" if insertado else "65 no fue insertado")
    print("Árbol final (inorden):", arbol.inorden())


if __name__ == "__main__":
    main()
