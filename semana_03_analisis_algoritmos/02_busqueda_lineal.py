"""Ejemplo 02: busqueda lineal y conteo de comparaciones.

La busqueda lineal revisa los elementos uno por uno hasta encontrar el valor
buscado o hasta terminar la lista.
"""


def busqueda_lineal(numeros: list[int], objetivo: int) -> tuple[int, int]:
    """Devuelve la posicion del objetivo y la cantidad de comparaciones."""
    comparaciones = 0

    for posicion, numero in enumerate(numeros):
        comparaciones += 1

        if numero == objetivo:
            return posicion, comparaciones

    return -1, comparaciones


def mostrar_resultado(numeros: list[int], objetivo: int) -> None:
    """Ejecuta una busqueda y muestra un resultado facil de leer."""
    posicion, comparaciones = busqueda_lineal(numeros, objetivo)

    print(f"Lista: {numeros}")
    print(f"Valor buscado: {objetivo}")

    if posicion == -1:
        print("Resultado: no encontrado")
    else:
        print(f"Resultado: encontrado en la posicion {posicion}")

    print(f"Comparaciones realizadas: {comparaciones}\n")


def main() -> None:
    numeros = [8, 14, 21, 32, 45, 60]

    print("Busqueda lineal")
    print("----------------")
    print("Caso 1: encontrado al inicio")
    mostrar_resultado(numeros, 8)

    print("Caso 2: encontrado al medio o final")
    mostrar_resultado(numeros, 45)

    print("Caso 3: no encontrado")
    mostrar_resultado(numeros, 99)

    print("Conclusion: en el peor caso se revisan todos los elementos.")


if __name__ == "__main__":
    main()
