"""Ejemplo 08: comparacion de busqueda en lista y conjunto."""

from time import perf_counter


def medir_busqueda(estructura, objetivo: int, nombre: str) -> None:
    inicio = perf_counter()
    encontrado = objetivo in estructura
    fin = perf_counter()

    print(f"Busqueda en {nombre}: {encontrado}")
    print(f"Tiempo aproximado: {fin - inicio:.10f} segundos\n")


def main() -> None:
    datos_lista = list(range(1_000_000))
    datos_conjunto = set(datos_lista)
    objetivo = 999_999

    # En una lista, Python puede tener que revisar muchos elementos.
    medir_busqueda(datos_lista, objetivo, "lista")

    # En un set, Python usa una estructura optimizada para busquedas.
    # Por eso suele encontrar valores mas rapido que en una lista grande.
    medir_busqueda(datos_conjunto, objetivo, "conjunto")


if __name__ == "__main__":
    main()

