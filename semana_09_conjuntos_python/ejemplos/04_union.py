"""Ejemplo 04: unir estudiantes de dos cursos."""


def main() -> None:
    """Reúne dos matrículas sin duplicar códigos comunes."""
    curso_a = {101, 102, 103, 104}
    curso_b = {103, 104, 105, 106}
    # Los códigos compartidos aparecen una sola vez en la unión.
    todos = curso_a | curso_b

    print("=== Ejemplo 04: Unión ===")
    print("Curso A:", sorted(curso_a))
    print("Curso B:", sorted(curso_b))
    print("Estudiantes de ambos cursos:", sorted(todos))


if __name__ == "__main__":
    main()
