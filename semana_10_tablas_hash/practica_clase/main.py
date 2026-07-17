"""Práctica: sistema de estudiantes con una tabla hash."""


class TablaHashEstudiantes:
    """Guarda estudiantes usando encadenamiento."""

    def __init__(self, tamanio=10):
        self.tabla = [[] for _ in range(tamanio)]
        self.cantidad = 0

    def calcular_indice(self, codigo):
        return codigo % len(self.tabla)

    def registrar(self, codigo, nombre):
        indice = self.calcular_indice(codigo)
        bucket = self.tabla[indice]
        print(f"Índice calculado: {indice}")

        for codigo_guardado, _ in bucket:
            if codigo_guardado == codigo:
                print("El código ya está registrado. No se agregó nuevamente.")
                return False

        if bucket:
            print("Aviso: hubo colisión, se guardó en el mismo bucket.")

        bucket.append((codigo, nombre))
        self.cantidad += 1
        print("Estudiante registrado correctamente.")
        return True

    def buscar(self, codigo):
        indice = self.calcular_indice(codigo)
        print(f"Índice calculado: {indice}")

        for codigo_guardado, nombre in self.tabla[indice]:
            if codigo_guardado == codigo:
                print(f"Estudiante encontrado: {nombre}")
                return nombre

        print("Estudiante no encontrado.")
        return None

    def eliminar(self, codigo):
        indice = self.calcular_indice(codigo)
        print(f"Índice calculado: {indice}")
        bucket = self.tabla[indice]

        for posicion, (codigo_guardado, nombre) in enumerate(bucket):
            if codigo_guardado == codigo:
                bucket.pop(posicion)
                self.cantidad -= 1
                print(f"Estudiante eliminado: {nombre}")
                return True

        print("Estudiante no encontrado; no se eliminó ningún registro.")
        return False

    def mostrar_tabla(self):
        print("\n=== TABLA HASH COMPLETA ===")
        for indice, bucket in enumerate(self.tabla):
            if bucket:
                datos = " -> ".join(
                    f"{codigo}: {nombre}" for codigo, nombre in bucket
                )
            else:
                datos = "Vacío"
            print(f"Índice {indice}: {datos}")

    def mostrar_colisiones(self):
        print("\n=== COLISIONES ===")
        hay_colisiones = False

        for indice, bucket in enumerate(self.tabla):
            if len(bucket) > 1:
                hay_colisiones = True
                print(f"Índice {indice}: {len(bucket)} estudiantes -> {bucket}")

        if not hay_colisiones:
            print("No hay colisiones en la tabla.")

    def mostrar_factor_carga(self):
        factor = self.cantidad / len(self.tabla)
        print(f"Elementos registrados: {self.cantidad}")
        print(f"Tamaño de la tabla: {len(self.tabla)}")
        print(f"Factor de carga: {factor:.2f}")

        if factor < 0.5:
            print("Bajo: pocas colisiones.")
        elif factor <= 0.75:
            print("Medio: se debe vigilar.")
        else:
            print("Alto: conviene redimensionar.")


def leer_codigo(mensaje):
    entrada = input(mensaje).strip()
    if not entrada.isdigit():
        print("Error: el código debe ser numérico.")
        return None
    return int(entrada)


def mostrar_menu():
    print("\n========================================")
    print(" SISTEMA DE TABLA HASH - ESTUDIANTES")
    print("========================================")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante por código")
    print("3. Eliminar estudiante")
    print("4. Mostrar tabla hash")
    print("5. Mostrar colisiones")
    print("6. Mostrar factor de carga")
    print("7. Salir")


def main():
    sistema = TablaHashEstudiantes(10)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = leer_codigo("Ingrese código: ")
            if codigo is None:
                continue

            nombre = input("Ingrese nombre: ").strip()
            if not nombre:
                print("Error: el nombre no puede estar vacío.")
                continue
            sistema.registrar(codigo, nombre)

        elif opcion == "2":
            codigo = leer_codigo("Ingrese código a buscar: ")
            if codigo is not None:
                sistema.buscar(codigo)

        elif opcion == "3":
            codigo = leer_codigo("Ingrese código a eliminar: ")
            if codigo is not None:
                sistema.eliminar(codigo)

        elif opcion == "4":
            sistema.mostrar_tabla()

        elif opcion == "5":
            sistema.mostrar_colisiones()

        elif opcion == "6":
            sistema.mostrar_factor_carga()

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Seleccione un número del 1 al 7.")


if __name__ == "__main__":
    main()
