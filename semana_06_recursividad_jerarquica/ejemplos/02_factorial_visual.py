def factorial(n, nivel=0):
    """
    Calcula el factorial de un número y muestra la profundidad de las llamadas.
    """
    indentacion = "  " * nivel
    print(f"{indentacion}Calculando factorial({n})")

    # Caso base:
    # factorial(1) ya se conoce, por eso no se necesita otra llamada.
    if n == 1:
        print(f"{indentacion}Caso base: factorial(1) = 1")
        return 1

    # Caso recursivo:
    # n se multiplica por el factorial de un número más pequeño.
    return n * factorial(n - 1, nivel + 1)


def main():
    resultado = factorial(5)
    print(f"Resultado final: {resultado}")


if __name__ == "__main__":
    main()
