"""Ejemplo 9: relacionar set y dict con tablas hash."""


codigos_matriculados = {205, 315, 428, 532}
estudiantes = {
    205: "Ana",
    315: "Carlos",
    428: "Elena",
    532: "Mario",
}

print("=== set: comprobar pertenencia ===")
print("¿El código 315 está matriculado?", 315 in codigos_matriculados)
print("¿El código 999 está matriculado?", 999 in codigos_matriculados)

print("\n=== dict: relacionar clave y valor ===")
print("Nombre del código 428:", estudiantes.get(428))
print("Nombre del código 999:", estudiantes.get(999, "No encontrado"))
