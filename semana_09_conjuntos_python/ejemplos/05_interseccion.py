"""Ejemplo 05: encontrar estudiantes comunes en dos grupos."""


def main() -> None:
    """Obtiene los códigos presentes en ambos conjuntos."""
    grupo_a = {101, 102, 103, 104}
    grupo_b = {103, 104, 105}
    # La intersección conserva únicamente los elementos comunes.
    comunes = grupo_a & grupo_b

    print("=== Ejemplo 05: Intersección ===")
    print("Grupo A:", sorted(grupo_a))
    print("Grupo B:", sorted(grupo_b))
    print("Estudiantes comunes:", sorted(comunes))


if __name__ == "__main__":
    main()
