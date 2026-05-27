"""Ejemplo 02: variables, tipos de datos y operadores."""


def main() -> None:
    # Tipos de datos basicos.
    edad = 20  # int: numero entero
    promedio = 86.5  # float: numero decimal
    nombre = "Ana"  # str: texto
    esta_aprobado = True  # bool: verdadero o falso
    esta_aprobado = "True"
    print("Tipos de datos")
    print(f"Nombre: {nombre} ({type(nombre).__name__})")
    print(f"Edad: {edad} ({type(edad).__name__})")
    print(f"Promedio: {promedio} ({type(promedio).__name__})")
    print(f"Esta aprobado: {esta_aprobado} ({type(esta_aprobado).__name__})")

    # Operadores aritmeticos.
    a = 10
    b = 3
    print("\nOperadores aritmeticos")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ** {b} = {a ** b}")

    # Operadores de comparacion.
    print("\nOperadores de comparacion")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")

    # Operadores logicos.
    tiene_asistencia = True
    tiene_nota_minima = promedio >= 71
    puede_aprobar = tiene_asistencia and tiene_nota_minima
    print("\nOperadores logicos")
    print(f"Tiene asistencia y nota minima: {puede_aprobar}")
    print(f"No tiene asistencia: {not tiene_asistencia}")

    # Mini caso: subtotal, impuesto y total.
    precio_unitario = 12.50
    cantidad = 4
    tasa_impuesto = 0.07
    subtotal = precio_unitario * cantidad
    impuesto = subtotal * tasa_impuesto
    total = subtotal + impuesto

    print("\nMini caso de factura")
    print(f"Subtotal: B/. {subtotal:.2f}")
    print(f"Impuesto: B/. {impuesto:.2f}")
    print(f"Total: B/. {total:.2f}")


if __name__ == "__main__":
    main()

