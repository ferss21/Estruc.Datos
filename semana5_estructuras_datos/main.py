from collections import deque

print("===== SEMANA 5: ESTRUCTURAS DE DATOS =====\n")

# LISTA:
# Se utiliza para guardar los estudiantes registrados.
estudiantes = ["Ana", "Luis", "Carlos", "María", "Pedro"]

print("Lista de estudiantes registrados:")
for i, estudiante in enumerate(estudiantes, start=1):
    print(f"{i}. {estudiante}")

print("\nCola de atención creada:")

# COLA:
# Se utiliza deque para simular una cola.
# En una cola, el primero que entra es el primero que sale.
cola_atencion = deque(estudiantes)

print(" -> ".join(cola_atencion))

# PILA:
# Se utiliza una lista para guardar el historial de atención.
# En una pila, el último que entra es el primero que sale.
historial_atencion = []

print("\nAtendiendo estudiantes:")

while cola_atencion:
    estudiante_atendido = cola_atencion.popleft()
    print(f"Atendiendo a: {estudiante_atendido}")
    historial_atencion.append(estudiante_atendido)

print("\nHistorial de atención usando pila:")

while historial_atencion:
    print(historial_atencion.pop())

# DICCIONARIO:
# Se utiliza para guardar información detallada de cada estudiante.
datos_estudiantes = {
    "Ana": {
        "carrera": "Ingeniería en Ciberseguridad",
        "semestre": 2,
        "estado": "Atendida",
    },
    "Luis": {
        "carrera": "Administración de Sistemas",
        "semestre": 3,
        "estado": "Atendido",
    },
    "Carlos": {
        "carrera": "Ingeniería en Ciberseguridad",
        "semestre": 1,
        "estado": "Atendido",
    },
    "María": {
        "carrera": "Administración de Sistemas",
        "semestre": 4,
        "estado": "Atendida",
    },
    "Pedro": {
        "carrera": "Ingeniería en Ciberseguridad",
        "semestre": 2,
        "estado": "Atendido",
    },
}

print("\nConsulta en diccionario:")

estudiante_consultado = "Ana"

print(f"Estudiante: {estudiante_consultado}")
print(f"Carrera: {datos_estudiantes[estudiante_consultado]['carrera']}")
print(f"Semestre: {datos_estudiantes[estudiante_consultado]['semestre']}")
print(f"Estado: {datos_estudiantes[estudiante_consultado]['estado']}")
