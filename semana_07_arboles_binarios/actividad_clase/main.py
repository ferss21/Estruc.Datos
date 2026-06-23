"""Actividad de clase: Sistema de Arbol Binario de Codigos Academicos."""


class Nodo:
    """Representa un codigo academico dentro del arbol."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Organiza codigos numericos usando un arbol binario de busqueda."""

    def __init__(self) -> None:
        self.raiz = None
        self.cantidad_nodos = 0

    def esta_vacio(self) -> bool:
        """Retorna True si el arbol no tiene nodos."""
        return self.raiz is None

    def insertar(self, codigo: int) -> bool:
        """Inserta un codigo y retorna False si ya existe."""
        if self.raiz is None:
            self.raiz = Nodo(codigo)
            self.cantidad_nodos += 1
            return True

        fue_insertado = self._insertar_recursivo(self.raiz, codigo)

        if fue_insertado:
            self.cantidad_nodos += 1

        return fue_insertado

    def _insertar_recursivo(self, nodo: Nodo, codigo: int) -> bool:
        """Busca la posicion correcta para insertar el codigo."""
        if codigo == nodo.dato:
            return False

        if codigo < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(codigo)
                return True

            return self._insertar_recursivo(nodo.izquierdo, codigo)

        if nodo.derecho is None:
            nodo.derecho = Nodo(codigo)
            return True

        return self._insertar_recursivo(nodo.derecho, codigo)

    def buscar(self, codigo: int) -> bool:
        """Retorna True si el codigo existe en el arbol."""
        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, nodo: Nodo | None, codigo: int) -> bool:
        """Busca un codigo comparando contra cada nodo visitado."""
        if nodo is None:
            return False

        if codigo == nodo.dato:
            return True

        if codigo < nodo.dato:
            return self._buscar_recursivo(nodo.izquierdo, codigo)

        return self._buscar_recursivo(nodo.derecho, codigo)

    def preorden(self) -> list[int]:
        """Retorna los codigos en recorrido preorden."""
        return self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo: Nodo | None) -> list[int]:
        """Visita raiz, izquierda y derecha."""
        if nodo is None:
            return []

        return (
            [nodo.dato]
            + self._preorden_recursivo(nodo.izquierdo)
            + self._preorden_recursivo(nodo.derecho)
        )

    def inorden(self) -> list[int]:
        """Retorna los codigos en recorrido inorden."""
        return self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo: Nodo | None) -> list[int]:
        """Visita izquierda, raiz y derecha."""
        if nodo is None:
            return []

        return (
            self._inorden_recursivo(nodo.izquierdo)
            + [nodo.dato]
            + self._inorden_recursivo(nodo.derecho)
        )

    def postorden(self) -> list[int]:
        """Retorna los codigos en recorrido postorden."""
        return self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo: Nodo | None) -> list[int]:
        """Visita izquierda, derecha y raiz."""
        if nodo is None:
            return []

        return (
            self._postorden_recursivo(nodo.izquierdo)
            + self._postorden_recursivo(nodo.derecho)
            + [nodo.dato]
        )

    def altura(self) -> int:
        """Retorna la altura del arbol contando niveles."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo: Nodo | None) -> int:
        """Calcula la mayor cantidad de niveles desde un nodo."""
        if nodo is None:
            return 0

        altura_izquierda = self._altura_recursiva(nodo.izquierdo)
        altura_derecha = self._altura_recursiva(nodo.derecho)

        return 1 + max(altura_izquierda, altura_derecha)

    def contar_hojas(self) -> int:
        """Retorna cuantas hojas tiene el arbol."""
        return self._contar_hojas_recursivo(self.raiz)

    def _contar_hojas_recursivo(self, nodo: Nodo | None) -> int:
        """Cuenta los nodos que no tienen hijos."""
        if nodo is None:
            return 0

        if nodo.izquierdo is None and nodo.derecho is None:
            return 1

        return self._contar_hojas_recursivo(nodo.izquierdo) + self._contar_hojas_recursivo(
            nodo.derecho
        )


def mostrar_menu() -> None:
    """Muestra las opciones disponibles."""
    print()
    print("=== Sistema de Arbol Binario de Codigos Academicos ===")
    print("1. Insertar codigo")
    print("2. Buscar codigo")
    print("3. Ver recorrido preorden")
    print("4. Ver recorrido inorden")
    print("5. Ver recorrido postorden")
    print("6. Ver altura del arbol")
    print("7. Contar hojas")
    print("8. Ver resumen")
    print("9. Salir")


def leer_codigo(mensaje: str) -> int:
    """Pide un codigo numerico hasta que el usuario escriba un entero valido."""
    while True:
        entrada = input(mensaje).strip()

        if entrada.isdigit():
            return int(entrada)

        print("Error: escriba un codigo numerico.")


def mostrar_lista(titulo: str, valores: list[int]) -> None:
    """Imprime una lista de codigos con un titulo."""
    print()
    print(f"{titulo}:")

    if valores:
        print(", ".join(str(valor) for valor in valores))
    else:
        print("El arbol esta vacio.")


def insertar_codigo(arbol: ArbolBinarioBusqueda) -> None:
    """Solicita un codigo y lo inserta en el arbol."""
    codigo = leer_codigo("Ingrese el codigo a insertar: ")

    if arbol.insertar(codigo):
        print(f"Codigo {codigo} insertado correctamente.")
    else:
        print(f"Codigo {codigo} ya existe. No se inserto de nuevo.")


def buscar_codigo(arbol: ArbolBinarioBusqueda) -> None:
    """Solicita un codigo y muestra si existe en el arbol."""
    if arbol.esta_vacio():
        print("El arbol esta vacio. No hay codigos para buscar.")
        return

    codigo = leer_codigo("Ingrese el codigo a buscar: ")

    if arbol.buscar(codigo):
        print(f"Codigo {codigo} encontrado.")
    else:
        print(f"Codigo {codigo} no existe.")


def mostrar_altura(arbol: ArbolBinarioBusqueda) -> None:
    """Muestra la altura del arbol."""
    if arbol.esta_vacio():
        print("El arbol esta vacio. Altura: 0")
    else:
        print(f"Altura del arbol: {arbol.altura()}")


def mostrar_hojas(arbol: ArbolBinarioBusqueda) -> None:
    """Muestra cuantas hojas tiene el arbol."""
    if arbol.esta_vacio():
        print("El arbol esta vacio. Cantidad de hojas: 0")
    else:
        print(f"Cantidad de hojas: {arbol.contar_hojas()}")


def mostrar_resumen(arbol: ArbolBinarioBusqueda) -> None:
    """Muestra un resumen general del arbol."""
    print()
    print("Resumen:")

    if arbol.esta_vacio():
        print("El arbol esta vacio.")
        print("Cantidad de nodos: 0")
        print("Cantidad de hojas: 0")
        print("Altura: 0")
        return

    print(f"Raiz: {arbol.raiz.dato}")
    print(f"Cantidad de nodos: {arbol.cantidad_nodos}")
    print(f"Cantidad de hojas: {arbol.contar_hojas()}")
    print(f"Altura: {arbol.altura()}")


def cargar_datos_prueba(arbol: ArbolBinarioBusqueda) -> None:
    """Carga codigos iniciales para probar rapidamente el programa."""
    for codigo in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(codigo)


def main() -> None:
    arbol = ArbolBinarioBusqueda()
    cargar_datos_prueba(arbol)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            insertar_codigo(arbol)
        elif opcion == "2":
            buscar_codigo(arbol)
        elif opcion == "3":
            mostrar_lista("Recorrido preorden", arbol.preorden())
        elif opcion == "4":
            mostrar_lista("Recorrido inorden", arbol.inorden())
        elif opcion == "5":
            mostrar_lista("Recorrido postorden", arbol.postorden())
        elif opcion == "6":
            mostrar_altura(arbol)
        elif opcion == "7":
            mostrar_hojas(arbol)
        elif opcion == "8":
            mostrar_resumen(arbol)
        elif opcion == "9":
            print("Saliendo del sistema.")
            break
        else:
            print("Opcion incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    main()
