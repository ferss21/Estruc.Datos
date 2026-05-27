"""Ejemplo 04: comparacion de tiempos entre ciclo y formula.

Este programa resuelve el mismo problema de dos maneras:
sumar los numeros del 1 hasta n usando un ciclo y usando una formula.
"""

from time import perf_counter


def sumar_con_ciclo(limite: int) -> tuple[int, int]:
    """Suma desde 1 hasta limite usando un ciclo."""
    total = 0
    operaciones = 0

    for numero in range(1, limite + 1):
        total += numero
        operaciones += 1  # Una suma principal por cada numero.

    return total, operaciones


def sumar_con_formula(limite: int) -> tuple[int, int]:
    """Suma desde 1 hasta limite usando la formula n * (n + 1) / 2."""
    total = limite * (limite + 1) // 2
    operaciones = 3  # Suma, multiplicacion y division entera.

    return total, operaciones


def medir_ciclo(limite: int) -> tuple[int, int, float]:
    """Mide el tiempo de la solucion con ciclo."""
    inicio = perf_counter()
    resultado, operaciones = sumar_con_ciclo(limite)
    fin = perf_counter()

    return resultado, operaciones, fin - inicio


def medir_formula(limite: int) -> tuple[int, int, float]:
    """Mide el tiempo de la solucion con formula."""
    inicio = perf_counter()
    resultado, operaciones = sumar_con_formula(limite)
    fin = perf_counter()

    return resultado, operaciones, fin - inicio


def main() -> None:
    limite = 100_000

    resultado_ciclo, operaciones_ciclo, tiempo_ciclo = medir_ciclo(limite)
    resultado_formula, operaciones_formula, tiempo_formula = medir_formula(limite)

    print("Comparacion de tiempos")
    print("-----------------------")
    print(f"Problema: sumar los numeros del 1 al {limite:,}\n")

    print("Solucion con ciclo")
    print(f"Resultado: {resultado_ciclo:,}")
    print(f"Operaciones contadas: {operaciones_ciclo:,}")
    print(f"Tiempo aproximado: {tiempo_ciclo:.8f} segundos\n")

    print("Solucion con formula")
    print(f"Resultado: {resultado_formula:,}")
    print(f"Operaciones contadas: {operaciones_formula}")
    print(f"Tiempo aproximado: {tiempo_formula:.8f} segundos\n")

    print("Conclusion: la formula realiza menos operaciones que el ciclo.")


if __name__ == "__main__":
    main()
