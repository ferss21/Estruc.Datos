"""Ejemplo 04: ciclos for y while."""


def main() -> None:
    numeros = [8, -3, 15, 0, 22, -7, 5]

    # for: se usa cuando queremos recorrer una secuencia.
    suma = 0
    for numero in numeros:
        suma += numero
    print(f"Suma de la lista: {suma}")

    positivos = 0
    for numero in numeros:
        if numero > 0:
            positivos += 1
    print(f"Cantidad de positivos: {positivos}")

    # enumerate permite obtener indice y valor al mismo tiempo.
    print("\nRecorrido con indice y valor")
    for indice, valor in enumerate(numeros):
        print(f"Indice {indice}: valor {valor}")

    # while: se usa cuando repetimos mientras una condicion sea verdadera.
    print("\nEjemplo con while")
    contador = 1
    while contador <= 5:
        print(f"Contador: {contador}")
        contador += 1


if __name__ == "__main__":
    main()

