"""Ejemplo 02: Cola de atención con deque.

Este programa muestra cómo una cola atiende tickets en orden de llegada.
La cola usa la regla FIFO: First In, First Out.
"""

from collections import deque


def mostrar_cola(cola_atencion: deque[int]) -> None:
    """Muestra los tickets en orden de atención."""
    print("Cola inicial: " + " -> ".join(str(ticket) for ticket in cola_atencion))


def atender_cola(cola_atencion: deque[int]) -> None:
    """Atiende todos los tickets usando popleft()."""
    while cola_atencion:
        ticket = cola_atencion.popleft()
        print(f"Atendiendo: {ticket}")

    print("Cola vacía.")


def main() -> None:
    # Este deque representa el TAD Cola.
    # En FIFO, el primer ticket que entra es el primero que sale.
    cola_atencion = deque()
    cola_atencion.append(101)
    cola_atencion.append(102)
    cola_atencion.append(103)

    print("=== Ejemplo 2: Cola de atención ===")
    mostrar_cola(cola_atencion)
    atender_cola(cola_atencion)


if __name__ == "__main__":
    main()
