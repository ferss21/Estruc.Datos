"""Laboratorio Semana 2: analisis basico de una lista de numeros.

Reto:
Completa las secciones marcadas con TODO para calcular:
- suma total
- cantidad de positivos
- numero mayor
- promedio
- conteo de operaciones principales
- tiempo aproximado de ejecucion
"""

from time import perf_counter


def analizar_numeros(numeros: list[float]) -> dict[str, float | int | None]:
    """Analiza una lista de numeros.

    Completa esta funcion como practica. Puedes usar ciclos, condicionales
    y variables auxiliares.
    """
    suma = 0
    positivos = 0
    mayor = None
    operaciones = 0

    inicio = perf_counter()

    # TODO: recorre la lista con un ciclo for.
    # TODO: suma cada numero en la variable suma.
    # TODO: cuenta cuantos numeros son positivos.
    # TODO: actualiza la variable mayor cuando encuentres un numero mas grande.
    # TODO: incrementa operaciones por cada elemento procesado.

    fin = perf_counter()

    # TODO: calcula el promedio. Recuerda validar si la lista esta vacia.
    promedio = 0

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

    print("Laboratorio Semana 2")
    print(f"Numeros: {numeros}")
    print(f"Suma total: {resultado['suma']}")
    print(f"Cantidad de positivos: {resultado['positivos']}")
    print(f"Numero mayor: {resultado['mayor']}")
    print(f"Promedio: {resultado['promedio']}")
    print(f"Operaciones principales: {resultado['operaciones']}")
    print(f"Tiempo aproximado: {resultado['tiempo']:.8f} segundos")


if __name__ == "__main__":
    main()

