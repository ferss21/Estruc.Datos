"""Ejemplo 08: validar subconjuntos y superconjuntos."""


def main() -> None:
    """Comprueba si las entregas pertenecen a la matrícula."""
    inscritos = {101, 102, 103, 104, 105}
    entregaron = {101, 103, 105}

    # Todas las entregas deben corresponder a estudiantes inscritos.
    print("=== Ejemplo 08: Subconjuntos ===")
    print("Inscritos:", sorted(inscritos))
    print("Entregaron:", sorted(entregaron))
    print("¿Entregaron es subconjunto de inscritos?", entregaron.issubset(inscritos))
    ## validar porque este mando valor true
    print("¿Inscritos es superconjunto de entregaron?", inscritos.issubset(entregaron))


if __name__ == "__main__":
    main()
