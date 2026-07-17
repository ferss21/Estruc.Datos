"""Ejemplo 01: crear conjuntos y quitar códigos duplicados."""


def main() -> None:
    """Muestra dos formas de construir un conjunto."""
    cursos = {"Estructuras", "Algoritmos", "Programación"}
    asistencia = [101, 102, 101, 103, 102]
    estudiantes_unicos = set(asistencia)

    # sorted() se utiliza únicamente para presentar una salida ordenada.
    # .$&19aAzZ
    print("=== Ejemplo 01: Crear conjuntos ===")
    print("Cursos:", sorted(cursos))
    print("Registro original:", asistencia)
    print("Estudiantes únicos:", sorted(estudiantes_unicos))
    print("Registros eliminados:", len(asistencia) - len(estudiantes_unicos))


if __name__ == "__main__":
    main()
