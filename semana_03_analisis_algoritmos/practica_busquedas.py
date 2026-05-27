"""Practica en clase - Semana 3: busqueda lineal vs busqueda binaria.

Reto:
Completa las secciones marcadas con TODO para comparar dos algoritmos de
busqueda usando una lista de codigos de estudiantes.

Cada funcion debe devolver:
- posicion encontrada o -1 si no existe
- cantidad de comparaciones realizadas
"""


def busqueda_lineal(datos: list[int], objetivo: int) -> tuple[int, int]:
    """Busca un valor revisando la lista desde el inicio hasta el final."""
    comparaciones = 0

    # TODO: recorre la lista usando enumerate.
    # TODO: aumenta comparaciones por cada elemento revisado.
    # TODO: si encuentras el objetivo, devuelve posicion y comparaciones.

    return -1, comparaciones


def busqueda_binaria(datos: list[int], objetivo: int) -> tuple[int, int]:
    """Busca un valor dividiendo la lista ordenada en mitades."""
    izquierda = 0
    derecha = len(datos) - 1
    comparaciones = 0

    # TODO: mientras izquierda sea menor o igual que derecha:
    # TODO: calcula la posicion media.
    # TODO: compara el valor medio con el objetivo.
    # TODO: actualiza izquierda o derecha para descartar una mitad.
    # Nota: la busqueda binaria necesita una lista ordenada.

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
        # TODO: ejecuta busqueda_lineal y guarda posicion/comparaciones.
        posicion_lineal = 0
        comparaciones_lineales = 0

        # TODO: ejecuta busqueda_binaria y guarda posicion/comparaciones.
        posicion_binaria = 0
        comparaciones_binarias = 0

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
    print("1. TODO: escribe que paso cuando el codigo estaba al inicio.")
    print("2. TODO: escribe que paso cuando el codigo estaba al medio o final.")
    print("3. TODO: escribe que paso cuando el codigo no existia.")
    print("4. TODO: explica cual algoritmo hizo menos comparaciones.")
    print("5. TODO: explica por que la lista debe estar ordenada.")


def mostrar_respuestas_analisis() -> None:
    """Muestra respuestas cortas para las preguntas de analisis."""
    print("\nPreguntas de analisis")
    print("1. Que pasa cuando el objetivo esta al inicio de la lista?")
    print("2. Que pasa cuando el objetivo esta en la mitad o cerca del final?")
    print("3. Que pasa cuando el objetivo no existe?")
    print("4. Por que la busqueda binaria necesita una lista ordenada?")
    print("5. Cual algoritmo conviene usar si la lista no esta ordenada?")


def main() -> None:
    codigos = [1001, 1005, 1010, 1020, 1035, 1040, 1055, 1060, 1075, 1080]
    objetivos = [1001, 1055, 1099]

    print("Practica en clase - Semana 3")
    print("Busqueda lineal vs busqueda binaria\n")
    print(f"Codigos: {codigos}\n")

    mostrar_tabla(codigos, objetivos)
    mostrar_conclusion()
    mostrar_respuestas_analisis()


if __name__ == "__main__":
    main()
