"""Ejemplo 06: identificar estudiantes pendientes de entrega."""


def main() -> None:
    """Resta las entregas al conjunto de estudiantes inscritos."""
    inscritos = {101, 102, 103, 104, 105}
    entregaron = {101, 103, 105}
    # El orden de la resta importa: se parte de todos los inscritos.
    pendientes = inscritos - entregaron

    print("=== Ejemplo 06: Diferencia ===")
    print("Inscritos:", sorted(inscritos))
    print("Entregaron:", sorted(entregaron))
    print("Pendientes:", sorted(pendientes))


if __name__ == "__main__":
    main()
