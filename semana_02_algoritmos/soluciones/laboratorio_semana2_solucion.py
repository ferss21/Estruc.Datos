"""Solucion del Laboratorio Semana 2."""

from time import perf_counter


def calcular_suma(numeros: list[float]) -> float:
    """Calcula la suma total de una lista de numeros."""
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


def contar_positivos(numeros: list[float]) -> int:
    """Cuenta cuantos numeros de la lista son mayores que cero."""
    positivos = 0
    for numero in numeros:
        if numero > 0:
            positivos += 1
    return positivos


def obtener_mayor(numeros: list[float]) -> float | None:
    """Devuelve el numero mayor o None si la lista esta vacia."""
    if not numeros:
        return None

    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor


def calcular_promedio(numeros: list[float]) -> float:
    """Calcula el promedio de una lista. Si esta vacia, devuelve 0."""
    if not numeros:
        return 0
    return calcular_suma(numeros) / len(numeros)


def analizar_numeros(numeros: list[float]) -> dict[str, float | int | None]:
    """Calcula indicadores principales y mide el tiempo aproximado."""
    suma = 0
    positivos = 0
    mayor = None
    operaciones = 0

    inicio = perf_counter()

    for numero in numeros:
        suma += numero
        operaciones += 1

        if numero > 0:
            positivos += 1

        if mayor is None or numero > mayor:
            mayor = numero

    promedio = suma / len(numeros) if numeros else 0

    fin = perf_counter()

    return {
        "suma": suma,
        "positivos": positivos,
        "mayor": mayor,
        "promedio": promedio,
        "operaciones": operaciones,
        "tiempo": fin - inicio,
    }


def main() -> None:
    numeros = [12, -4, 7, 0, 25, -10, 8]
    resultado = analizar_numeros(numeros)

    print("Solucion Laboratorio Semana 2")
    print(f"Numeros: {numeros}")
    print(f"Suma total: {resultado['suma']}")
    print(f"Cantidad de positivos: {resultado['positivos']}")
    print(f"Numero mayor: {resultado['mayor']}")
    print(f"Promedio: {resultado['promedio']:.2f}")
    print(f"Operaciones principales: {resultado['operaciones']}")
    print(f"Tiempo aproximado: {resultado['tiempo']:.8f} segundos")


if __name__ == "__main__":
    main()

