"""Ejemplo 01: TAD Lista en Python.

Este programa simula una lista de estudiantes. La lista funciona como un Tipo
Abstracto de Datos porque usamos funciones para agregar, listar, buscar,
actualizar y eliminar elementos.
"""


def agregar_estudiante(estudiantes: list[str], nombre: str) -> None:
    """Agrega un estudiante al final de la lista."""
    estudiantes.append(nombre)


def listar_estudiantes(estudiantes: list[str]) -> None:
    """Muestra todos los estudiantes registrados."""
    if not estudiantes:
        print("La lista esta vacia.")
        return

    for posicion, nombre in enumerate(estudiantes):
        print(f"{posicion}. {nombre}")


def buscar_estudiante(estudiantes: list[str], nombre: str) -> int:
    """Busca un estudiante y devuelve su posicion o -1 si no existe."""
    for posicion, estudiante in enumerate(estudiantes):
        if estudiante == nombre:
            return posicion

    return -1


def actualizar_estudiante(estudiantes: list[str], anterior: str, nuevo: str) -> bool:
    """Actualiza el nombre de un estudiante si existe."""
    posicion = buscar_estudiante(estudiantes, anterior)

    if posicion == -1:
        return False

    estudiantes[posicion] = nuevo
    return True


def eliminar_estudiante(estudiantes: list[str], nombre: str) -> bool:
    """Elimina un estudiante si existe en la lista."""
    posicion = buscar_estudiante(estudiantes, nombre)

    if posicion == -1:
        return False

    estudiantes.pop(posicion)
    return True


def main() -> None:
    # Este list representa el TAD Lista.
    estudiantes = ["Ana", "Luis", "Marta"]

    print("=== TAD LISTA ===")
    print("Datos iniciales:")
    listar_estudiantes(estudiantes)

    print("\nAgregar estudiante: Carlos")
    agregar_estudiante(estudiantes, "Carlos")
    listar_estudiantes(estudiantes)

    print("\nBuscar estudiante: Luis")
    posicion = buscar_estudiante(estudiantes, "Luis")
    print(f"Resultado de busqueda: posicion {posicion}")

    print("\nActualizar estudiante: Marta -> Maria")
    actualizado = actualizar_estudiante(estudiantes, "Marta", "Maria")
    print(f"Actualizado: {actualizado}")
    listar_estudiantes(estudiantes)

    print("\nEliminar estudiante: Ana")
    eliminado = eliminar_estudiante(estudiantes, "Ana")
    print(f"Eliminado: {eliminado}")
    listar_estudiantes(estudiantes)


if __name__ == "__main__":
    main()
