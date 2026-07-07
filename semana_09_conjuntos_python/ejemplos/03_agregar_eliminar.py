"""Ejemplo 03: agregar y eliminar códigos de una matrícula."""


def main() -> None:
    """Compara add(), remove() y discard()."""
    inscritos = {101, 102, 103}
    print("=== Ejemplo 03: Agregar y eliminar ===")
    print("Estado inicial:", sorted(inscritos))

    inscritos.add(104)
    inscritos.remove(102)  # remove exige que el elemento exista.
    inscritos.discard(999)  # discard no falla si el elemento no existe.

    print("Después de agregar 104 y eliminar 102:", sorted(inscritos))
    print("discard(999) no produjo error.")
    print("remove(999) produciría KeyError porque 999 no está registrado.")


if __name__ == "__main__":
    main()
