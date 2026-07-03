"""Reto 01: completar una búsqueda que también devuelva la ruta visitada."""


class Nodo:
    """Guarda un dato y los enlaces del árbol."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """Árbol de apoyo para practicar una búsqueda iterativa."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta valores sin duplicarlos."""
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

    def buscar_con_ruta(self, valor: int) -> tuple[bool, list[int]]:
        """Debe buscar el valor y guardar cada nodo visitado."""
        ruta: list[int] = []
        actual = self.raiz

        # TODO: mientras actual no sea None, agregar su dato a ruta.
        # TODO: retornar True si coincide y avanzar a la rama correcta si no.
        # Pista: use actual.izquierdo cuando valor < actual.dato.
        _ = valor, actual
        return False, ruta


def main() -> None:
    """Ejecuta dos pruebas que permiten comprobar la solución."""
    arbol = ArbolBinarioBusqueda()
    datos = [50, 30, 70, 20, 40, 60, 80]
    for valor in datos:
        arbol.insertar(valor)

    print("=== Reto 01: Completar búsqueda con ruta ===")
    print("Datos de prueba:", datos)
    print("Resultado esperado para 40: (True, [50, 30, 40])")
    print("Resultado obtenido para 40:", arbol.buscar_con_ruta(40))
    print("Resultado esperado para 99: (False, [50, 70, 80])")
    print("Resultado obtenido para 99:", arbol.buscar_con_ruta(99))


if __name__ == "__main__":
    main()

