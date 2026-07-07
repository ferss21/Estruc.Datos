"""Ejemplo 02: comprobar la asistencia de estudiantes."""


def main() -> None:
    """Aplica los operadores in y not in sobre un conjunto."""
    asistieron = {101, 103, 105}
    codigo_buscado = 103
    codigo_ausente = 104

    print("=== Ejemplo 02: Pertenencia ===")
    print("Asistencia:", sorted(asistieron))
    print(f"¿Asistió {codigo_buscado}?", codigo_buscado in asistieron)
    print(f"¿Faltó {codigo_ausente}?", codigo_ausente not in asistieron)


if __name__ == "__main__":
    main()
