universidad = {
    "Estudiantes": {
        "Matrícula": {
            "solicitudes.pdf": None,
            "calendario.pdf": None
        },
        "Notas": {
            "reporte_notas.xlsx": None
        }
    },
    "Profesores": {
        "Planificaciones": {
            "semana6.docx": None
        }
    },
    "Laboratorios": {
        "Python": {
            "practica_recursividad.py": None
        },
        "Redes": {}
    }
}


def mostrar_menu():
    print()
    print("=== EXPLORADOR JERÁRQUICO ACADÉMICO ===")
    print("1. Mostrar estructura completa")
    print("2. Contar archivos")
    print("3. Buscar archivo por nombre")
    print("4. Calcular profundidad máxima")
    print("5. Salir")


def mostrar_estructura(estructura, nivel=0):
    """
    Muestra carpetas y archivos con indentación según su nivel.
    """
    for nombre, contenido in estructura.items():
        indentacion = "  " * nivel

        if isinstance(contenido, dict):
            print(f"{indentacion}{nombre}/")

            # Caso recursivo:
            # Si el elemento es una carpeta, se recorren sus elementos internos.
            mostrar_estructura(contenido, nivel + 1)
        else:
            # Caso base:
            # Si el elemento es un archivo, se imprime y no se baja más.
            print(f"{indentacion}{nombre}")


def contar_archivos(estructura):
    """
    Cuenta cuántos archivos existen dentro de toda la jerarquía.
    """
    total = 0

    for contenido in estructura.values():
        if isinstance(contenido, dict):
            # Caso recursivo:
            # Si es carpeta, se cuentan los archivos que tiene dentro.
            total += contar_archivos(contenido)
        else:
            # Caso base:
            # Si es archivo, suma 1 al total.
            total += 1

    return total


def buscar_archivo(estructura, nombre):
    """
    Busca un archivo por nombre dentro de la jerarquía.
    """
    for elemento, contenido in estructura.items():
        if contenido is None and elemento == nombre:
            # Caso base:
            # El archivo fue encontrado.
            return True

        if isinstance(contenido, dict):
            # Caso recursivo:
            # Si es carpeta, se busca dentro de esa carpeta.
            if buscar_archivo(contenido, nombre):
                return True

    # Caso base:
    # Se revisó esta parte de la jerarquía y no se encontró el archivo.
    return False


def profundidad_maxima(estructura):
    """
    Calcula la profundidad máxima de carpetas en la jerarquía.
    """
    if not estructura:
        # Caso base:
        # Una carpeta vacía no agrega más niveles.
        return 0

    profundidad_mayor = 0

    for contenido in estructura.values():
        if isinstance(contenido, dict):
            # Caso recursivo:
            # Se baja a la carpeta interna y se suma el nivel actual.
            profundidad = 1 + profundidad_maxima(contenido)
        else:
            # Caso base:
            # Un archivo representa el último nivel de la ruta.
            profundidad = 1

        if profundidad > profundidad_mayor:
            profundidad_mayor = profundidad

    return profundidad_mayor


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_estructura(universidad)
        elif opcion == "2":
            print(f"Total de archivos: {contar_archivos(universidad)}")
        elif opcion == "3":
            nombre = input("Ingrese el archivo a buscar: ")

            if buscar_archivo(universidad, nombre):
                print(f"Archivo encontrado: {nombre}")
            else:
                print(f"Archivo no encontrado: {nombre}")
        elif opcion == "4":
            print(f"Profundidad máxima: {profundidad_maxima(universidad)}")
        elif opcion == "5":
            print("Saliendo del explorador.")
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    main()
