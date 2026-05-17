"""Ejemplo 07: conteo de operaciones principales."""


def sumar_y_contar(numeros: list[int]) -> tuple[int, int]:
    """Suma valores y cuenta cuantas sumas principales se realizan."""
    suma = 0
    operaciones = 0

    for numero in numeros:
        suma += numero
        operaciones += 1  # Contamos la operacion principal: sumar un valor.

    return suma, operaciones


def main() -> None:
    numeros = [10, 20, 30, 40, 50]
    suma, operaciones = sumar_y_contar(numeros)

    print(f"Resultado de la suma: {suma}")
    print(f"Operaciones principales realizadas: {operaciones}")


if __name__ == "__main__":
    main()

