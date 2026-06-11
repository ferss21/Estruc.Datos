"""Ejemplo 04: Lista de tickets atendidos.

Este programa muestra cómo una lista almacena tickets atendidos en orden.
"""


def mostrar_tickets_atendidos(tickets_atendidos: list[dict[str, str]]) -> None:
    """Recorre la lista de tickets atendidos con for."""
    print("Tickets atendidos:")
    for posicion, ticket in enumerate(tickets_atendidos, start=1):
        print(f"{posicion}. {ticket['codigo']} - {ticket['estudiante']}")


def main() -> None:
    # Este list permite almacenar datos en orden.
    tickets_atendidos = [
        {"codigo": "101", "estudiante": "Ana"},
        {"codigo": "102", "estudiante": "Luis"},
        {"codigo": "103", "estudiante": "María"},
    ]

    print("=== Ejemplo 4: Lista de tickets atendidos ===")
    mostrar_tickets_atendidos(tickets_atendidos)
    print(f"\nTotal atendidos: {len(tickets_atendidos)}")


if __name__ == "__main__":
    main()
