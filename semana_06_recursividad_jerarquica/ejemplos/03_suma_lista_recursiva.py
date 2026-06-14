def suma_recursiva(lista):
    """
    Suma los elementos de una lista usando recursividad.
    """
    # Caso base:
    # Una lista vacía no tiene elementos, por eso su suma es 0.
    if len(lista) == 0:
        return 0

    # Caso recursivo:
    # Se toma el primer elemento y se suma con el resto de la lista.
    return lista[0] + suma_recursiva(lista[1:])


def main():
    numeros = [10, 20, 30, 40]
    print(f"Lista: {numeros}")
    print(f"Suma total: {suma_recursiva(numeros)}")


if __name__ == "__main__":
    main()
