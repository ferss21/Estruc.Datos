"""Tarea evaluada: analizar matrícula y entregas de dos grupos."""


def obtener_estudiantes_unicos(codigos: list[int]) -> set[int]:
    """Debe convertir una lista de códigos en un conjunto."""
    # TODO: elimine los duplicados y retorne el conjunto resultante.
    _ = codigos
    return set()


def obtener_estudiantes_comunes(grupo_a: set[int],
                                grupo_b: set[int]) -> set[int]:
    """Debe obtener los estudiantes presentes en ambos grupos."""
    # TODO: aplique la operación de intersección.
    _ = grupo_a, grupo_b
    return set()


def obtener_estudiantes_exclusivos(grupo_a: set[int],
                                   grupo_b: set[int]) -> set[int]:
    """Debe obtener los códigos que aparecen en un solo grupo."""
    # TODO: aplique la operación de diferencia simétrica.
    _ = grupo_a, grupo_b
    return set()


def obtener_pendientes(inscritos: set[int],
                       entregaron: set[int]) -> set[int]:
    """Debe obtener los inscritos que todavía no entregaron."""
    # TODO: reste las entregas al conjunto de inscritos.
    _ = inscritos, entregaron
    return set()


def entregas_validas(inscritos: set[int], entregaron: set[int]) -> bool:
    """Debe comprobar si las entregas son un subconjunto de inscritos."""
    # TODO: use issubset() para realizar la validación.
    _ = inscritos, entregaron
    return False


def main() -> None:
    """Ejecuta el caso de prueba utilizado para evaluar la actividad."""
    lista_a = [101, 102, 103, 104, 101]
    lista_b = [103, 104, 105, 106, 105]
    entregaron = {101, 103, 105}

    grupo_a = obtener_estudiantes_unicos(lista_a)
    grupo_b = obtener_estudiantes_unicos(lista_b)
    inscritos = grupo_a | grupo_b

    print("=== Tarea evaluada: Control de entregas por grupos ===")
    print("Grupo A esperado: [101, 102, 103, 104]")
    print("Grupo A obtenido:", sorted(grupo_a))
    print("Grupo B esperado: [103, 104, 105, 106]")
    print("Grupo B obtenido:", sorted(grupo_b))
    print("Comunes esperados: [103, 104]")
    print("Comunes obtenidos:", sorted(obtener_estudiantes_comunes(grupo_a, grupo_b)))
    print("Exclusivos esperados: [101, 102, 105, 106]")
    print("Exclusivos obtenidos:", sorted(obtener_estudiantes_exclusivos(grupo_a, grupo_b)))
    print("Pendientes esperados: [102, 104, 106]")
    print("Pendientes obtenidos:", sorted(obtener_pendientes(inscritos, entregaron)))
    print("Entregas válidas esperadas: True")
    print("Entregas válidas obtenidas:", entregas_validas(inscritos, entregaron))


if __name__ == "__main__":
    main()
