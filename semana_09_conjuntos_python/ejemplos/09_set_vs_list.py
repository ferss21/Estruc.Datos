"""Ejemplo 09: comparar una lista con un conjunto."""


def main() -> None:
    """Señala cuándo importa repetir datos y cuándo importa la unicidad."""
    registros = [101, 102, 101, 103, 102]
    # La conversión elimina repeticiones, no modifica la lista original.
    estudiantes = set(registros)

    print("=== Ejemplo 09: set frente a list ===")
    print("Lista de registros:", registros)
    print("Cantidad de registros:", len(registros))
    print("Conjunto de estudiantes:", sorted(estudiantes))
    print("Cantidad de estudiantes únicos:", len(estudiantes))
    print("La lista conserva cada registro; el set conserva cada código una vez.")


if __name__ == "__main__":
    main()
