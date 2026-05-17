"""Ejemplo 03: condicionales para clasificar una nota."""


def clasificar_nota(nota: float) -> str:
    """Devuelve la clasificacion de una nota entre 0 y 100."""
    if nota < 0 or nota > 100:
        return "Nota invalida. Debe estar entre 0 y 100."

    if nota >= 91:
        return "Excelente"
    if nota >= 71:
        return "Aprobado"
    return "Reprobado"


def main() -> None:
    nota = float(input("Ingrese una nota entre 0 y 100: "))
    clasificacion = clasificar_nota(nota)
    print(f"Resultado: {clasificacion}")


if __name__ == "__main__":
    main()

