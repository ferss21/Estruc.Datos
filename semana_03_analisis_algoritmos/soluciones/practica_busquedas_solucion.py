"""Solucion de la practica en clase - Semana 3.

Tema: comparacion entre busqueda lineal y busqueda binaria con conteo de
comparaciones.
"""


def busqueda_lineal(datos: list[int], objetivo: int) -> tuple[int, int]:
    """Busca un valor revisando la lista desde el inicio hasta el final."""
    comparaciones = 0

    for posicion, valor in enumerate(datos):
        comparaciones += 1

        if valor == objetivo:
            return posicion, comparaciones

    return -1, comparaciones


def busqueda_binaria(datos: list[int], objetivo: int) -> tuple[int, int]:
    """Busca un valor dividiendo una lista ordenada en mitades."""
    izquierda = 0
    derecha = len(datos) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = datos[medio]
        comparaciones += 1

        if valor_medio == objetivo:
            return medio, comparaciones

        # Como la lista esta ordenada, podemos descartar una mitad.
        if objetivo < valor_medio:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return -1, comparaciones


def mostrar_tabla(codigos: list[int], objetivos: list[int]) -> None:
    """Ejecuta ambas busquedas y muestra una tabla de resultados."""
    encabezado = (
        "Objetivo | Pos. lineal | Comp. lineales | Pos. binaria | "
        "Comp. binarias"
    )

    print(encabezado)
    print("-" * len(encabezado))

    for objetivo in objetivos:
        posicion_lineal, comparaciones_lineales = busqueda_lineal(codigos, objetivo)
        posicion_binaria, comparaciones_binarias = busqueda_binaria(codigos, objetivo)

        print(
            f"{objetivo:<8} | "
            f"{posicion_lineal:^12} | "
            f"{comparaciones_lineales:^15} | "
            f"{posicion_binaria:^13} | "
            f"{comparaciones_binarias:^15}"
        )


def mostrar_conclusion() -> None:
    """Muestra una conclusion breve de cinco lineas."""
    print("\nConclusion")
    print("1. La busqueda lineal fue mejor cuando el codigo estaba al inicio.")
    print("2. Para codigos mas alejados, la busqueda lineal hizo mas comparaciones.")
    print("3. La busqueda binaria dividio la lista en mitades en cada paso.")
    print("4. Por eso, la busqueda binaria fue mas eficiente en la mayoria de casos.")
    print("5. La busqueda binaria solo funciona correctamente con listas ordenadas.")


def mostrar_respuestas_analisis() -> None:
    """Muestra respuestas cortas para las preguntas de analisis."""
    print("\nPreguntas de analisis")
    print("1. Si el objetivo esta al inicio, la busqueda lineal lo encuentra rapido.")
    print("2. Si esta al medio o final, la busqueda lineal necesita mas comparaciones.")
    print("3. Si no existe, la busqueda lineal revisa toda la lista.")
    print("4. La busqueda binaria necesita orden para descartar mitades correctamente.")
    print("5. Si la lista no esta ordenada, conviene usar busqueda lineal.")


def main() -> None:
    codigos = [1001, 1005, 1010, 1020, 1035, 1040, 1055, 1060, 1075, 1080]
    objetivos = [1001, 1055, 1099]

    print("Solucion practica en clase - Semana 3")
    print("Busqueda lineal vs busqueda binaria\n")
    print(f"Codigos: {codigos}\n")

    mostrar_tabla(codigos, objetivos)
    mostrar_conclusion()
    mostrar_respuestas_analisis()


if __name__ == "__main__":
    main()
