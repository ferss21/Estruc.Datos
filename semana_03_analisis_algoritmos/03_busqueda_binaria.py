"""Ejemplo 03: busqueda binaria y conteo de comparaciones.

La busqueda binaria divide el espacio de busqueda a la mitad en cada paso.
Para funcionar correctamente, la lista debe estar ordenada.
"""


def busqueda_binaria(numeros: list[int], objetivo: int) -> tuple[int, int]:
    """Devuelve la posicion del objetivo y la cantidad de comparaciones."""
    izquierda = 0
    derecha = len(numeros) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1

        if numeros[medio] == objetivo:
            return medio, comparaciones

        # La lista debe estar ordenada para saber que mitad descartar.
        if objetivo < numeros[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return -1, comparaciones


def mostrar_resultado(numeros: list[int], objetivo: int) -> None:
    """Ejecuta una busqueda binaria y muestra el resultado."""
    posicion, comparaciones = busqueda_binaria(numeros, objetivo)

    print(f"Lista ordenada: {numeros}")
    print(f"Valor buscado: {objetivo}")

    if posicion == -1:
        print("Resultado: no encontrado")
    else:
        print(f"Resultado: encontrado en la posicion {posicion}")

    print(f"Comparaciones realizadas: {comparaciones}\n")


def main() -> None:
    numeros = [3, 9, 12, 18, 25, 31, 42, 56, 70]

    print("Busqueda binaria")
    print("-----------------")
    mostrar_resultado(numeros, 25)
    mostrar_resultado(numeros, 70)
    mostrar_resultado(numeros, 100)

    print("Conclusion: al dividir la lista, se hacen menos comparaciones.")


if __name__ == "__main__":
    main()
