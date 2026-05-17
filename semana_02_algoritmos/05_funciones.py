"""Ejemplo 05: funciones reutilizables."""


def calcular_promedio(notas: list[float]) -> float:
    """Calcula el promedio de una lista de notas.

    Si la lista esta vacia, devuelve 0 para evitar division entre cero.
    """
    if not notas:
        return 0
    return sum(notas) / len(notas)


def contar_positivos(numeros: list[float]) -> int:
    """Cuenta cuantos numeros de la lista son mayores que cero."""
    cantidad = 0
    for numero in numeros:
        if numero > 0:
            cantidad += 1
    return cantidad


def obtener_mayor(numeros: list[float]) -> float | None:
    """Devuelve el numero mayor de una lista.

    Si la lista esta vacia, devuelve None porque no existe un mayor.
    """
    if not numeros:
        return None

    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor


def clasificar_nota(nota: float) -> str:
    """Clasifica una nota entre 0 y 100."""
    if nota < 0 or nota > 100:
        return "Invalida"
    if nota >= 91:
        return "Excelente"
    if nota >= 71:
        return "Aprobado"
    return "Reprobado"


def main() -> None:
    notas = [78, 95, 62, 88]
    numeros = [4, -2, 15, 0, 9]

    print(f"Promedio de notas: {calcular_promedio(notas):.2f}")
    print(f"Positivos: {contar_positivos(numeros)}")
    print(f"Mayor: {obtener_mayor(numeros)}")
    print(f"Clasificacion de 95: {clasificar_nota(95)}")


if __name__ == "__main__":
    main()

