"""Ejemplo 03: Recorridos de un arbol binario de busqueda."""


class Nodo:
    """Representa un nodo de un arbol binario de busqueda."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


def insertar(raiz: Nodo | None, valor: int) -> Nodo:
    """Inserta un valor y retorna la raiz actualizada."""
    if raiz is None:
        return Nodo(valor)

    if valor < raiz.dato:
        raiz.izquierdo = insertar(raiz.izquierdo, valor)
    elif valor > raiz.dato:
        raiz.derecho = insertar(raiz.derecho, valor)

    return raiz


def preorden(nodo: Nodo | None) -> list[int]:
    """Recorre primero la raiz, luego izquierda y derecha."""
    if nodo is None:
        return []

    return [nodo.dato] + preorden(nodo.izquierdo) + preorden(nodo.derecho)


def inorden(nodo: Nodo | None) -> list[int]:
    """Recorre izquierda, raiz y derecha."""
    if nodo is None:
        return []

    return inorden(nodo.izquierdo) + [nodo.dato] + inorden(nodo.derecho)


def postorden(nodo: Nodo | None) -> list[int]:
    """Recorre izquierda, derecha y al final la raiz."""
    if nodo is None:
        return []

    return postorden(nodo.izquierdo) + postorden(nodo.derecho) + [nodo.dato]


def mostrar_recorrido(nombre: str, valores: list[int]) -> None:
    """Imprime un recorrido como texto separado por comas."""
    print(f"{nombre}: {', '.join(str(valor) for valor in valores)}")


def main() -> None:
    raiz = None
    valores = [50, 30, 70, 20, 40, 60, 80]

    for valor in valores:
        raiz = insertar(raiz, valor)

    print("=== Ejemplo 3: Recorridos ===")
    print("Preorden visita primero la raiz.")
    print("Inorden muestra los valores ordenados en un BST.")
    print("Postorden visita la raiz al final.")
    print()

    mostrar_recorrido("Preorden", preorden(raiz))
    mostrar_recorrido("Inorden", inorden(raiz))
    mostrar_recorrido("Postorden", postorden(raiz))


if __name__ == "__main__":
    main()
