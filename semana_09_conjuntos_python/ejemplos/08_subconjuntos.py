"""Ejemplo 08: validar subconjuntos y superconjuntos."""


def main() -> None:
    """Comprueba si las entregas pertenecen a la matrícula."""
    inscritos = {101, 102, 103, 104, 105}
    entregaron = {101, 103, 105}

    print("=== Ejemplo 08: Subconjuntos ===")
    print("Inscritos:", sorted(inscritos))
    print("Entregaron:", sorted(entregaron))
    print("¿Entregaron es subconjunto de inscritos?", entregaron.issubset(inscritos))
    print("¿Inscritos es superconjunto de entregaron?", inscritos.issuperset(entregaron))


if __name__ == "__main__":
    main()
