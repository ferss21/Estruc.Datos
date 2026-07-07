"""Ejemplo 12: representar un conjunto mediante una lista interna."""


class ConjuntoSimple:
    """Guarda enteros sin duplicarlos y ofrece operaciones básicas."""

    def __init__(self, valores: list[int] | None = None) -> None:
        self.elementos: list[int] = []
        for valor in valores or []:
            self.agregar(valor)

    def agregar(self, valor: int) -> bool:
        """Agrega el valor solamente si todavía no existe."""
        if self.contiene(valor):
            return False
        self.elementos.append(valor)
        return True

    def eliminar(self, valor: int) -> bool:
        """Elimina un valor y avisa si fue encontrado."""
        if not self.contiene(valor):
            return False
        self.elementos.remove(valor)
        return True

    def contiene(self, valor: int) -> bool:
        """Comprueba pertenencia dentro de la lista interna."""
        return valor in self.elementos

    def union(self, otro: "ConjuntoSimple") -> "ConjuntoSimple":
        """Crea un conjunto nuevo con los elementos de ambos."""
        resultado = ConjuntoSimple(self.elementos)
        for valor in otro.elementos:
            resultado.agregar(valor)
        return resultado

    def interseccion(self, otro: "ConjuntoSimple") -> "ConjuntoSimple":
        """Crea un conjunto nuevo con los elementos comunes."""
        resultado = ConjuntoSimple()
        for valor in self.elementos:
            if otro.contiene(valor):
                resultado.agregar(valor)
        return resultado

    def mostrar(self) -> list[int]:
        """Devuelve una copia ordenada para presentar el contenido."""
        return sorted(self.elementos)


def main() -> None:
    """Prueba las operaciones con dos grupos académicos."""
    grupo_a = ConjuntoSimple([101, 102, 102, 103])
    grupo_b = ConjuntoSimple([103, 104, 105])
    grupo_a.agregar(106)
    grupo_a.eliminar(102)

    print("=== Ejemplo 12: Conjunto personalizado ===")
    print("Grupo A:", grupo_a.mostrar())
    print("Grupo B:", grupo_b.mostrar())
    print("¿A contiene 101?", grupo_a.contiene(101))
    print("Unión:", grupo_a.union(grupo_b).mostrar())
    print("Intersección:", grupo_a.interseccion(grupo_b).mostrar())


if __name__ == "__main__":
    main()
