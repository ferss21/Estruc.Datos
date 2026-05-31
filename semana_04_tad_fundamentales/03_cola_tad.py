"""Ejemplo 03: TAD Cola en Python.

Este programa simula una cola de atencion de estudiantes. La cola usa la regla
FIFO: First In, First Out. Es decir, el primero en llegar es el primero en ser
atendido.
"""

from collections import deque


def agregar_a_cola(cola: deque[str], nombre: str) -> None:
    """Agrega un estudiante al final de la cola."""
    cola.append(nombre)


def atender_primero(cola: deque[str]) -> str | None:
    """Atiende y elimina al primer estudiante de la cola."""
    if not cola:
        return None

    return cola.popleft()


def ver_proximo(cola: deque[str]) -> str | None:
    """Devuelve el proximo estudiante sin eliminarlo."""
    if not cola:
        return None

    return cola[0]


def mostrar_cola(cola: deque[str]) -> None:
    """Muestra todos los estudiantes en orden de atencion."""
    if not cola:
        print("La cola esta vacia.")
        return

    print("Inicio -> Final")
    for nombre in cola:
        print(f"- {nombre}")


def main() -> None:
    # Este deque representa el TAD Cola.
    cola_estudiantes = deque(["Daniel", "Elena", "Fabio"])

    print("=== TAD COLA ===")
    print("Datos iniciales:")
    mostrar_cola(cola_estudiantes)

    print("\nAgregar a la cola: Gabriela")
    agregar_a_cola(cola_estudiantes, "Gabriela")
    mostrar_cola(cola_estudiantes)

    print("\nVer proximo estudiante")
    print(f"Proximo: {ver_proximo(cola_estudiantes)}")

    print("\nAtender el primero")
    atendido = atender_primero(cola_estudiantes)
    print(f"Estudiante atendido: {atendido}")
    mostrar_cola(cola_estudiantes)

    print("\nConclusion: la cola atiende primero a quien llego primero.")


if __name__ == "__main__":
    main()
