"""Ejemplo 04: TAD Correspondencia en Python.

Este programa simula registros de estudiantes usando un diccionario. La clave
es el codigo del estudiante y el valor es su nombre.
"""


def agregar_registro(registros: dict[int, str], codigo: int, nombre: str) -> None:
    """Agrega un nuevo registro al diccionario."""
    registros[codigo] = nombre


def buscar_por_clave(registros: dict[int, str], codigo: int) -> str | None:
    """Busca un registro por codigo y devuelve el nombre."""
    return registros.get(codigo)


def actualizar_registro(registros: dict[int, str], codigo: int, nombre: str) -> bool:
    """Actualiza un registro si el codigo existe."""
    if codigo not in registros:
        return False

    registros[codigo] = nombre
    return True


def eliminar_registro(registros: dict[int, str], codigo: int) -> bool:
    """Elimina un registro si el codigo existe."""
    if codigo not in registros:
        return False

    del registros[codigo]
    return True


def mostrar_registros(registros: dict[int, str]) -> None:
    """Muestra todos los registros guardados."""
    if not registros:
        print("No hay registros.")
        return

    for codigo, nombre in registros.items():
        print(f"{codigo}: {nombre}")


def main() -> None:
    # Este dict representa el TAD Correspondencia.
    estudiantes = {
        1001: "Ana",
        1005: "Luis",
        1010: "Marta",
    }

    print("=== TAD CORRESPONDENCIA ===")
    print("Datos iniciales:")
    mostrar_registros(estudiantes)

    print("\nAgregar registro: 1020 -> Carlos")
    agregar_registro(estudiantes, 1020, "Carlos")
    mostrar_registros(estudiantes)

    print("\nBuscar clave: 1005")
    nombre = buscar_por_clave(estudiantes, 1005)
    print(f"Resultado: {nombre}")

    print("\nActualizar registro: 1010 -> Maria")
    actualizado = actualizar_registro(estudiantes, 1010, "Maria")
    print(f"Actualizado: {actualizado}")
    mostrar_registros(estudiantes)

    print("\nEliminar registro: 1001")
    eliminado = eliminar_registro(estudiantes, 1001)
    print(f"Eliminado: {eliminado}")
    mostrar_registros(estudiantes)


if __name__ == "__main__":
    main()
