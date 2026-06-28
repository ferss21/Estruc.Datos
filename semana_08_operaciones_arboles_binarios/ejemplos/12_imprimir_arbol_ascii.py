"""Ejemplo 12: dibujar un BST mediante texto e indentación."""


class Nodo:
    """Representa un nodo que se mostrará en el dibujo textual."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """BST con una representación jerárquica sencilla."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Agrega valores únicos a la estructura."""
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

    def lineas_ascii(self) -> list[str]:
        """Crea líneas con etiquetas para raíz, izquierda y derecha."""
        if self.raiz is None:
            return ["(árbol vacío)"]
        lineas = [f"RAÍZ: {self.raiz.dato}"]

        def dibujar(nodo: Nodo | None, prefijo: str, etiqueta: str) -> None:
            if nodo is None:
                lineas.append(f"{prefijo}{etiqueta}: vacío")
                return
            lineas.append(f"{prefijo}{etiqueta}: {nodo.dato}")
            # Cada nivel agrega indentación para hacer visible la jerarquía.
            dibujar(nodo.izquierdo, prefijo + "    ", "IZQ")
            dibujar(nodo.derecho, prefijo + "    ", "DER")

        dibujar(self.raiz.izquierdo, "    ", "IZQ")
        dibujar(self.raiz.derecho, "    ", "DER")
        return lineas

    def imprimir_ascii(self) -> None:
        """Imprime todas las líneas de la representación."""
        for linea in self.lineas_ascii():
            print(linea)


def main() -> None:
    """Construye el árbol base y muestra su forma."""
    arbol = ArbolBinarioBusqueda()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    print("=== Ejemplo 12: Representación ASCII del árbol ===")
    arbol.imprimir_ascii()
    print("Las etiquetas indican qué rama ocupa cada valor.")


if __name__ == "__main__":
    main()

