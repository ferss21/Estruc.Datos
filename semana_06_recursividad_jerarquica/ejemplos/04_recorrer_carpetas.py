def recorrer_carpetas(estructura, nivel=0):
    """
    Recorre una estructura de carpetas anidadas usando recursividad.
    """
    for nombre, contenido in estructura.items():
        indentacion = "  " * nivel
        print(f"{indentacion}{nombre}")

        # Caso recursivo:
        # Si el contenido es otro diccionario, se baja un nivel en la jerarquía.
        if isinstance(contenido, dict):
            recorrer_carpetas(contenido, nivel + 1)

        # Caso base:
        # Una carpeta vacía no contiene más elementos para recorrer.


def main():
    universidad = {
        "Universidad": {
            "Estudiantes": {
                "Matrícula": {},
                "Notas": {}
            },
            "Profesores": {},
            "Laboratorios": {
                "Python": {},
                "Redes": {}
            }
        }
    }

    recorrer_carpetas(universidad)


if __name__ == "__main__":
    main()
