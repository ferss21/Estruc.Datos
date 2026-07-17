"""Ejemplo 10: combinar asistencia en set y notas en dict."""


def main() -> None:
    """Cruza códigos únicos con información asociada a cada código."""
    asistieron = {101, 103, 105, 106}
    notas = {101: 92, 102: 78, 103: 85, 105: 95}

    print("=== Ejemplo 10: set y dict ===")
    print("Asistieron:", sorted(asistieron))
    print("Notas de quienes asistieron:")
    for codigo in sorted(asistieron):
        # get permite mostrar un mensaje aunque todavía no exista una nota.
        print(f"Estudiante {codigo}: {notas.get(codigo, 'sin nota')}")


if __name__ == "__main__":
    main()
