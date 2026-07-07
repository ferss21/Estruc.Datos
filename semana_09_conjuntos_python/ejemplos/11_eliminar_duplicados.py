"""Ejemplo 11: devolver códigos únicos a partir de una lista."""


def obtener_unicos(codigos: list[int]) -> set[int]:
    """Convierte la lista recibida en un conjunto."""
    return set(codigos)


def main() -> None:
    """Prueba la función con registros académicos repetidos."""
    codigos = [201, 202, 201, 203, 204, 202, 204]
    unicos = obtener_unicos(codigos)

    print("=== Ejemplo 11: Eliminar duplicados ===")
    print("Códigos recibidos:", codigos)
    print("Códigos únicos:", sorted(unicos))


if __name__ == "__main__":
    main()
