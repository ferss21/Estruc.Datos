"""Ejemplo 06: medicion aproximada de tiempo de ejecucion."""

from time import perf_counter


def sumar_numeros(cantidad: int) -> int:
    """Suma los numeros desde 0 hasta cantidad - 1."""
    total = 0
    for numero in range(cantidad):
        total += numero
    return total


def medir_suma(cantidad: int) -> None:
    inicio = perf_counter()
    resultado = sumar_numeros(cantidad)
    fin = perf_counter()

    tiempo = fin - inicio
    print(f"Suma de {cantidad:,} elementos: {resultado}")
    print(f"Tiempo aproximado: {tiempo:.8f} segundos\n")


def main() -> None:
    # El tiempo puede variar segun la computadora y los programas abiertos.
    medir_suma(100)
    medir_suma(100_000)


if __name__ == "__main__":
    main()

