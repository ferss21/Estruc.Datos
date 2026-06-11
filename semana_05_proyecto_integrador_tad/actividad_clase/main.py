"""Actividad de clase - Semana 5: sistema de tickets académicos.

Este programa integra lista, pila, cola y diccionario en un sistema pequeño de
atención de tickets académicos.
"""

from collections import deque


# Diccionario: guarda cada ticket usando el código como clave.
tickets: dict[int, dict[str, str | int]] = {}

# Cola: controla el orden de atención con la regla FIFO.
cola_atencion: deque[int] = deque()

# Pila: guarda acciones. La última acción debe mostrarse primero.
historial_acciones: list[str] = []

# Lista: almacena los tickets que ya fueron atendidos.
tickets_atendidos: list[dict[str, str | int]] = []


def mostrar_menu() -> None:
    """Muestra las opciones principales del sistema."""
    print("\n=== SISTEMA DE TICKETS ACADÉMICOS ===")
    print("1. Registrar ticket")
    print("2. Agregar ticket a la cola")
    print("3. Atender siguiente ticket")
    print("4. Buscar ticket por código")
    print("5. Ver historial de acciones")
    print("6. Ver resumen del sistema")
    print("7. Salir")


def registrar_ticket() -> None:
    """Registra un ticket nuevo en el diccionario."""
    codigo_texto = input("Ingrese el código del ticket: ").strip()

    if not codigo_texto.isdigit():
        print("El código debe ser un número.")
        return

    codigo = int(codigo_texto)

    if codigo in tickets:
        print(f"Ya existe un ticket con código {codigo}.")
        return

    estudiante = input("Nombre del estudiante: ").strip()
    carrera = input("Carrera: ").strip()
    motivo = input("Motivo: ").strip()

    if estudiante == "" or carrera == "" or motivo == "":
        print("Todos los campos son obligatorios.")
        return

    tickets[codigo] = {
        "codigo": codigo,
        "estudiante": estudiante,
        "carrera": carrera,
        "motivo": motivo,
        "estado": "Registrado",
    }
    historial_acciones.append(f"REGISTRADO {codigo}")
    print(f"Ticket {codigo} registrado correctamente.")


def agregar_a_cola() -> None:
    """Agrega un ticket existente a la cola de atención."""
    codigo_texto = input("Ingrese el código del ticket: ").strip()

    if not codigo_texto.isdigit():
        print("El código debe ser un número.")
        return

    codigo = int(codigo_texto)

    if codigo not in tickets:
        print(f"No existe un ticket con código {codigo}.")
        return

    if tickets[codigo]["estado"] == "En cola":
        print(f"El ticket {codigo} ya está en la cola.")
        return

    if tickets[codigo]["estado"] == "Atendido":
        print(f"El ticket {codigo} ya fue atendido.")
        return

    cola_atencion.append(codigo)
    tickets[codigo]["estado"] = "En cola"
    historial_acciones.append(f"ENCOLADO {codigo}")
    print(f"Ticket {codigo} agregado a la cola.")


def atender_ticket() -> None:
    """Atiende el siguiente ticket según el orden de llegada."""
    if not cola_atencion:
        print("No hay tickets en la cola de atención.")
        return

    codigo = cola_atencion.popleft()
    tickets[codigo]["estado"] = "Atendido"
    tickets_atendidos.append(tickets[codigo])
    historial_acciones.append(f"ATENDIDO {codigo}")

    ticket = tickets[codigo]

    print("Atendiendo ticket:")
    print(f"Código: {ticket['codigo']}")
    print(f"Estudiante: {ticket['estudiante']}")
    print(f"Carrera: {ticket['carrera']}")
    print(f"Motivo: {ticket['motivo']}")
    print(f"Estado: {ticket['estado']}")


def buscar_ticket() -> None:
    """Busca un ticket por código en el diccionario."""
    codigo_texto = input("Ingrese el código del ticket: ").strip()

    if not codigo_texto.isdigit():
        print("El código debe ser un número.")
        return

    codigo = int(codigo_texto)
    ticket = tickets.get(codigo)

    if ticket is None:
        print(f"No existe un ticket con código {codigo}.")
        return

    historial_acciones.append(f"BUSCADO {codigo}")

    print("Ticket encontrado:")
    print(f"Código: {ticket['codigo']}")
    print(f"Estudiante: {ticket['estudiante']}")
    print(f"Carrera: {ticket['carrera']}")
    print(f"Motivo: {ticket['motivo']}")
    print(f"Estado: {ticket['estado']}")


def ver_historial() -> None:
    """Muestra el historial como pila, desde la acción más reciente."""
    if not historial_acciones:
        print("No hay acciones registradas.")
        return

    print("Historial de acciones:")
    for accion in reversed(historial_acciones):
        print(accion)


def ver_resumen() -> None:
    """Muestra un resumen de las estructuras del sistema."""
    print("Resumen del sistema:")
    print(f"Tickets registrados: {len(tickets)}")
    print(f"Tickets en cola: {len(cola_atencion)}")
    print(f"Tickets atendidos: {len(tickets_atendidos)}")
    print(f"Acciones en historial: {len(historial_acciones)}")


def cargar_datos_prueba() -> None:
    """Carga automáticamente los tickets iniciales para la actividad."""
    tickets[101] = {
        "codigo": 101,
        "estudiante": "Ana",
        "carrera": "Ingeniería en Ciberseguridad",
        "motivo": "Consulta de matrícula",
        "estado": "Registrado",
    }
    tickets[102] = {
        "codigo": 102,
        "estudiante": "Luis",
        "carrera": "Administración de Sistemas",
        "motivo": "Soporte de plataforma",
        "estado": "Registrado",
    }
    tickets[103] = {
        "codigo": 103,
        "estudiante": "María",
        "carrera": "Ingeniería en Ciberseguridad",
        "motivo": "Solicitud de laboratorio",
        "estado": "Registrado",
    }
    historial_acciones.append("DATOS DE PRUEBA CARGADOS")


if __name__ == "__main__":
    cargar_datos_prueba()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_ticket()
        elif opcion == "2":
            agregar_a_cola()
        elif opcion == "3":
            atender_ticket()
        elif opcion == "4":
            buscar_ticket()
        elif opcion == "5":
            ver_historial()
        elif opcion == "6":
            ver_resumen()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Seleccione un número del 1 al 7.")
