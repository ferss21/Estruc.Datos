"""Práctica: sistema de análisis de grupos académicos con conjuntos.

El programa permite modificar matrícula, asistencia y entregas. Los resultados
se ordenan únicamente al imprimirlos para facilitar su lectura.
"""


def mostrar_menu() -> None:
    """Presenta las opciones disponibles."""
    print("\n=== Sistema de análisis de grupos académicos con conjuntos ===")
    print("1. Registrar estudiantes inscritos")
    print("2. Registrar asistencia")
    print("3. Registrar entregas")
    print("4. Ver estudiantes únicos")
    print("5. Ver quienes asistieron y entregaron")
    print("6. Ver pendientes de entrega")
    print("7. Ver inscritos que no asistieron")
    print("8. Comparar dos grupos")
    print("9. Mostrar resumen")
    print("10. Salir")


def leer_codigo(mensaje: str) -> int:
    """Repite la solicitud hasta recibir un código numérico entero."""
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit():
            return int(entrada)
        print("Código no válido. Escriba solamente números.")


def mostrar_conjunto(titulo: str, datos: set[int]) -> None:
    """Muestra los elementos ordenados o informa que no existen datos."""
    if datos:
        print(f"{titulo}: {sorted(datos)}")
    else:
        print(f"{titulo}: no hay datos registrados.")


def modificar_registro(nombre: str, datos: set[int], inscritos: set[int]) -> None:
    """Permite agregar o eliminar un código de un conjunto."""
    print(f"\n1. Agregar código a {nombre}")
    print(f"2. Eliminar código de {nombre}")
    accion = input("Seleccione una acción: ").strip()
    if accion not in {"1", "2"}:
        print("Acción no válida.")
        return

    codigo = leer_codigo("Código del estudiante: ")
    if accion == "1":
        # La asistencia y las entregas solo aceptan estudiantes inscritos.
        if datos is not inscritos and codigo not in inscritos:
            print(f"El código {codigo} no está inscrito.")
        elif codigo in datos:
            print(f"El código {codigo} ya estaba registrado; no se duplicó.")
        else:
            datos.add(codigo)
            print(f"Código {codigo} agregado a {nombre}.")
    elif codigo in datos:
        datos.remove(codigo)
        print(f"Código {codigo} eliminado de {nombre}.")
    else:
        print(f"El código {codigo} no se encuentra en {nombre}.")


def registrar_inscritos(inscritos: set[int], asistieron: set[int],
                        entregaron: set[int]) -> None:
    """Modifica matrícula y mantiene relacionados los otros registros."""
    cantidad_antes = len(inscritos)
    modificar_registro("inscritos", inscritos, inscritos)
    # Si se retiró una matrícula, también se limpia de asistencia y entregas.
    if len(inscritos) < cantidad_antes:
        asistieron.intersection_update(inscritos)
        entregaron.intersection_update(inscritos)


def comparar_grupos(inscritos: set[int]) -> None:
    """Lee un segundo grupo y aplica cuatro operaciones de conjuntos."""
    entrada = input("Códigos del grupo B separados por espacios: ").split()
    if not entrada:
        print("No se ingresaron códigos para el grupo B.")
        return
    if not all(codigo.isdigit() for codigo in entrada):
        print("Grupo no válido. Todos los códigos deben ser numéricos.")
        return
    grupo_b = {int(codigo) for codigo in entrada}
    mostrar_conjunto("Unión", inscritos | grupo_b)
    mostrar_conjunto("Intersección", inscritos & grupo_b)
    mostrar_conjunto("Solo en inscritos", inscritos - grupo_b)
    mostrar_conjunto("Exclusivos de cada grupo", inscritos ^ grupo_b)


def mostrar_resumen(inscritos: set[int], asistieron: set[int],
                    entregaron: set[int]) -> None:
    """Presenta los registros y sus cantidades actuales."""
    print("\n--- Resumen académico ---")
    mostrar_conjunto("Inscritos", inscritos)
    mostrar_conjunto("Asistieron", asistieron)
    mostrar_conjunto("Entregaron", entregaron)
    print("Cantidad de inscritos:", len(inscritos))
    print("Cantidad de asistentes:", len(asistieron))
    print("Cantidad de entregas:", len(entregaron))


def main() -> None:
    """Ejecuta el menú hasta seleccionar la opción de salida."""
    inscritos = {101, 102, 103, 104, 105, 106}
    asistieron = {101, 103, 105}
    entregaron = {101, 102, 105}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_inscritos(inscritos, asistieron, entregaron)
        elif opcion == "2":
            modificar_registro("asistencia", asistieron, inscritos)
        elif opcion == "3":
            modificar_registro("entregas", entregaron, inscritos)
        elif opcion == "4":
            mostrar_conjunto("Estudiantes únicos", inscritos)
        elif opcion == "5":
            mostrar_conjunto("Asistieron y entregaron", asistieron & entregaron)
        elif opcion == "6":
            mostrar_conjunto("Pendientes de entrega", inscritos - entregaron)
        elif opcion == "7":
            mostrar_conjunto("Inscritos que no asistieron", inscritos - asistieron)
        elif opcion == "8":
            comparar_grupos(inscritos)
        elif opcion == "9":
            mostrar_resumen(inscritos, asistieron, entregaron)
        elif opcion == "10":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Seleccione un número del 1 al 10.")


if __name__ == "__main__":
    main()
