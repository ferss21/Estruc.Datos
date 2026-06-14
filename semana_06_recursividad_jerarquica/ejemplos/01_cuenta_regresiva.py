def cuenta_regresiva(n):
    """
    Muestra una cuenta regresiva usando recursividad.
    """
    print(n)

    # Caso base:
    # Si n llega a 0, la función deja de llamarse a sí misma.
    if n == 0:
        print("Fin de la recursividad")
        return

    # Caso recursivo:
    # La función se llama con un problema más pequeño: n - 1.
    cuenta_regresiva(n - 1)


def main():
    print("Cuenta regresiva:")
    cuenta_regresiva(5)


if __name__ == "__main__":
    main()
