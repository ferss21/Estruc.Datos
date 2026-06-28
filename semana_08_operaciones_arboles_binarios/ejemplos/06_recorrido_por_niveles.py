"""Ejemplo 06: recorrer un árbol nivel por nivel con una lista."""

# La cola conserva el orden en que se descubren los nodos de cada nivel.

class Nodo:
    """Representa un valor y sus posibles hijos."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST que agrupa los datos según su nivel."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta un valor usando comparaciones iterativas."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True
        actual = self.raiz
        while True:
            if valor == actual.dato:
                return False
            atributo = "izquierdo" if valor < actual.dato else "derecho"
            siguiente = getattr(actual, atributo)
            if siguiente is None:
                setattr(actual, atributo, Nodo(valor))
                return True
            actual = siguiente

    def recorrido_por_niveles(self) -> list[list[int]]:
        """Usa una lista como cola simple y conserva el número de nivel."""
        if self.raiz is None:
            return []
        cola: list[tuple[Nodo, int]] = [(self.raiz, 0)]
        posicion = 0
        niveles: list[list[int]] = []
        while posicion < len(cola):
            nodo, nivel = cola[posicion]
            posicion += 1
            if nivel == len(niveles):
                niveles.append([])
            niveles[nivel].append(nodo.dato)
            if nodo.izquierdo is not None:
                cola.append((nodo.izquierdo, nivel + 1))
            if nodo.derecho is not None:
                cola.append((nodo.derecho, nivel + 1))
        return niveles


def main() -> None:
    """Imprime claramente los niveles 0, 1 y 2."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    print("=== Ejemplo 06: Recorrido por niveles ===")
    for numero, valores in enumerate(arbol.recorrido_por_niveles()):
        print(f"Nivel {numero}:", " ".join(str(valor) for valor in valores))
    print("Orden completo: 50 -> 30 -> 70 -> 20 -> 40 -> 60 -> 80")


if __name__ == "__main__":
    main()
