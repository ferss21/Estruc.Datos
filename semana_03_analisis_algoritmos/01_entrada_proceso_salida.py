"""Ejemplo 01: entrada, proceso y salida con conteo de operaciones.

Este programa usa una lista de ventas como entrada, calcula el total y el
promedio como proceso, y muestra los resultados como salida.

Tambien cuenta operaciones basicas para introducir el analisis de algoritmos.
"""


def analizar_ventas(ventas: list[float]) -> tuple[float, float, int]:
    """Calcula el total, el promedio y cuenta operaciones basicas."""
    total = 0.0
    operaciones = 0

    # Recorremos cada venta una vez.
    for venta in ventas:
        total += venta
        operaciones += 1  # Una suma principal.

    promedio = total / len(ventas)
    operaciones += 1  # Una division para calcular el promedio.

    return total, promedio, operaciones


def main() -> None:
    # ENTRADA: datos iniciales del problema.
    ventas = [120.50, 80.00, 45.75, 200.00, 150.25]

    # PROCESO: calculos realizados por el algoritmo.
    total, promedio, operaciones = analizar_ventas(ventas)

    # SALIDA: informacion visible para el usuario.
    print("Analisis de ventas")
    print("------------------")
    print(f"Ventas registradas: {ventas}")
    print(f"Total vendido: B/. {total:.2f}")
    print(f"Promedio de venta: B/. {promedio:.2f}")
    print(f"Operaciones basicas contadas: {operaciones}")
    print("Conclusion: al aumentar las ventas, aumenta el recorrido del ciclo.")


if __name__ == "__main__":
    main()
