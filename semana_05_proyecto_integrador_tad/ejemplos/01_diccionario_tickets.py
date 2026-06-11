"""Ejemplo 01: Diccionario de tickets académicos.

Este programa muestra cómo usar un diccionario para guardar tickets por código.
La clave permite encontrar un ticket específico de forma directa.
"""


def mostrar_tickets(tickets: dict[int, dict[str, str]]) -> None:
    """Muestra todos los tickets registrados."""
    for codigo, ticket in tickets.items():
        print(f"{codigo} - {ticket['estudiante']} - {ticket['motivo']}")


def buscar_ticket(tickets: dict[int, dict[str, str]], codigo: int) -> None:
    """Busca un ticket usando su código como clave."""
    ticket = tickets.get(codigo)

    if ticket is None:
        print(f"No existe un ticket con código {codigo}.")
        return

    print(
        "Ticket encontrado: "
        f"{codigo} - {ticket['estudiante']} - {ticket['motivo']}"
    )


def main() -> None:
    # Este dict representa una correspondencia: código -> datos del ticket.
    # Sirve para buscar rápidamente por clave.
    tickets = {
        101: {
            "estudiante": "Ana",
            "carrera": "Ingeniería en Ciberseguridad",
            "motivo": "Consulta de matrícula",
            "estado": "Registrado",
        },
        102: {
            "estudiante": "Luis",
            "carrera": "Administración de Sistemas",
            "motivo": "Soporte de plataforma",
            "estado": "Registrado",
        },
        103: {
            "estudiante": "María",
            "carrera": "Ingeniería en Ciberseguridad",
            "motivo": "Solicitud de laboratorio",
            "estado": "Registrado",
        },
    }

    print("=== Ejemplo 1: Diccionario de tickets ===")
    print("Tickets registrados:")
    mostrar_tickets(tickets)

    print("\nBúsqueda por código:")
    buscar_ticket(tickets, 102)


if __name__ == "__main__":
    main()
