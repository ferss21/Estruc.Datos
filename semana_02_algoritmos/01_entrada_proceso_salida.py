"""Ejemplo 01: entrada, proceso y salida.

Este programa recibe dos notas, calcula el promedio y muestra el resultado.
Puede ejecutarse directamente desde la terminal:

    python 01_entrada_proceso_salida.py
"""


def main() -> None:
    # ENTRADA: datos que el programa necesita para trabajar.
    nota_1 = float(input("Ingrese la primera nota: "))
    nota_2 = float(input("Ingrese la segunda nota: "))

    # PROCESO: operaciones que transforman la entrada.
    promedio = (nota_1 + nota_2 + 30) / 10

    # SALIDA: resultado que se muestra al usuario.
    print(f"El promedio es: {promedio:.2f}")


if __name__ == "__main__":
    main()

