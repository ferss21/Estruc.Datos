"""Ejemplo 07: encontrar estudiantes exclusivos de cada grupo."""


def main() -> None:
    """Descarta los códigos compartidos entre dos grupos."""
    grupo_a = {101, 102, 103, 104}
    grupo_b = {103, 104, 105, 106}
    exclusivos = grupo_a ^ grupo_b

    print("=== Ejemplo 07: Diferencia simétrica ===")
    print("Grupo A:", sorted(grupo_a))
    print("Grupo B:", sorted(grupo_b))
    print("En un solo grupo:", sorted(exclusivos))


if __name__ == "__main__":
    main()
