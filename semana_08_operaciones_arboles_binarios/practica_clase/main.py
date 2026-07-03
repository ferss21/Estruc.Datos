"""Práctica de clase: operaciones con un árbol binario de búsqueda.

DIRECTRIZ DE LA ACTIVIDAD
Ejecute el programa y utilice el menú para practicar la inserción, búsqueda,
recorridos, medición y eliminación de valores en un árbol binario de búsqueda.
Compruebe después de cada modificación que el recorrido inorden permanece
ordenado de menor a mayor.

CASO PRÁCTICO
El programa inicia con los valores 50, 30, 70, 20, 40, 60 y 80.

1. Muestre el resumen inicial del árbol.
2. Busque 40 y 99 para observar una búsqueda exitosa y una fallida.
3. Inserte 65 e intente insertar nuevamente 50 para comprobar que no se
   admiten valores duplicados.
4. Elimine 20 para aplicar el caso de un nodo hoja.
5. Elimine 60 para aplicar el caso de un nodo con un hijo.
6. Elimine 70 para aplicar el caso de un nodo con dos hijos.
7. Muestre el recorrido inorden y el resumen después de cada eliminación para
   verificar que el árbol conserva la propiedad de búsqueda.
"""


class Nodo:
    """Almacena un entero y referencias a sus hijos."""

    def __init__(self, dato: int) -> None:
        self.dato = dato
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None


class ArbolBinarioBusqueda:
    """Agrupa operaciones de consulta, recorrido, medición y modificación."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def esta_vacio(self) -> bool:
        """Indica si todavía no existe una raíz."""
        return self.raiz is None

    def insertar(self, valor: int) -> bool:
        """Inserta un entero; retorna False para un valor duplicado."""
        insertado, self.raiz = self._insertar(self.raiz, valor)
        return insertado

    def _insertar(self, nodo: Nodo | None, valor: int) -> tuple[bool, Nodo]:
        if nodo is None:
            return True, Nodo(valor)
        if valor == nodo.dato:
            return False, nodo
        if valor < nodo.dato:
            insertado, nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        else:
            insertado, nodo.derecho = self._insertar(nodo.derecho, valor)
        return insertado, nodo

    def buscar_con_ruta(self, valor: int) -> tuple[bool, list[int]]:
        """Busca sobre una sola rama y registra cada nodo comparado."""
        ruta: list[int] = []
        actual = self.raiz
        while actual is not None:
            ruta.append(actual.dato)
            if valor == actual.dato:
                return True, ruta
            actual = actual.izquierdo if valor < actual.dato else actual.derecho
        return False, ruta

    def _buscar_nodo(self, valor: int) -> Nodo | None:
        """Localiza un nodo para poder describir su caso de eliminación."""
        actual = self.raiz
        while actual is not None:
            if valor == actual.dato:
                return actual
            actual = actual.izquierdo if valor < actual.dato else actual.derecho
        return None

    def inorden(self) -> list[int]:
        """Visita izquierda, raíz y derecha; en un BST queda ordenado."""
        return self._inorden(self.raiz)

    def _inorden(self, nodo: Nodo | None) -> list[int]:
        if nodo is None:
            return []
        return self._inorden(nodo.izquierdo) + [nodo.dato] + self._inorden(nodo.derecho)

    def preorden(self) -> list[int]:
        """Visita raíz, izquierda y derecha."""
        return self._preorden(self.raiz)

    def _preorden(self, nodo: Nodo | None) -> list[int]:
        if nodo is None:
            return []
        return [nodo.dato] + self._preorden(nodo.izquierdo) + self._preorden(nodo.derecho)

    def postorden(self) -> list[int]:
        """Visita izquierda, derecha y raíz."""
        return self._postorden(self.raiz)

    def _postorden(self, nodo: Nodo | None) -> list[int]:
        if nodo is None:
            return []
        return self._postorden(nodo.izquierdo) + self._postorden(nodo.derecho) + [nodo.dato]

    def recorrido_por_niveles(self) -> list[list[int]]:
        """Agrupa nodos por profundidad utilizando una lista como cola."""
        if self.raiz is None:
            return []
        pendientes: list[tuple[Nodo, int]] = [(self.raiz, 0)]
        posicion = 0
        niveles: list[list[int]] = []
        while posicion < len(pendientes):
            nodo, nivel = pendientes[posicion]
            posicion += 1
            if nivel == len(niveles):
                niveles.append([])
            niveles[nivel].append(nodo.dato)
            if nodo.izquierdo is not None:
                pendientes.append((nodo.izquierdo, nivel + 1))
            if nodo.derecho is not None:
                pendientes.append((nodo.derecho, nivel + 1))
        return niveles

    def altura(self) -> int:
        """Mide en aristas: hoja 0 y árbol vacío -1."""
        return self._altura(self.raiz)

    def _altura(self, nodo: Nodo | None) -> int:
        if nodo is None:
            return -1
        return 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))

    def contar_nodos(self) -> int:
        """Cuenta cada nodo una vez mediante un recorrido completo."""
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo: Nodo | None) -> int:
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)

    def contar_hojas(self) -> int:
        """Cuenta únicamente nodos que no tienen hijos."""
        return self._contar_hojas(self.raiz)

    def _contar_hojas(self, nodo: Nodo | None) -> int:
        if nodo is None:
            return 0
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1
        return self._contar_hojas(nodo.izquierdo) + self._contar_hojas(nodo.derecho)

    def minimo(self) -> int | None:
        """Retorna el extremo izquierdo o None para un árbol vacío."""
        if self.raiz is None:
            return None
        return self._nodo_minimo(self.raiz).dato

    def maximo(self) -> int | None:
        """Retorna el extremo derecho o None para un árbol vacío."""
        actual = self.raiz
        if actual is None:
            return None
        while actual.derecho is not None:
            actual = actual.derecho
        return actual.dato

    def _nodo_minimo(self, nodo: Nodo) -> Nodo:
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def describir_caso(self, valor: int) -> str | None:
        """Describe cuántos hijos tiene el nodo antes de eliminarlo."""
        nodo = self._buscar_nodo(valor)
        if nodo is None:
            return None
        hijos = int(nodo.izquierdo is not None) + int(nodo.derecho is not None)
        return ["hoja", "un hijo", "dos hijos"][hijos]

    def eliminar(self, valor: int) -> bool:
        """Elimina un valor resolviendo los tres casos estructurales."""
        self.raiz, eliminado = self._eliminar(self.raiz, valor)
        return eliminado

    def _eliminar(self, nodo: Nodo | None, valor: int) -> tuple[Nodo | None, bool]:
        if nodo is None:
            return None, False
        if valor < nodo.dato:
            nodo.izquierdo, eliminado = self._eliminar(nodo.izquierdo, valor)
            return nodo, eliminado
        if valor > nodo.dato:
            nodo.derecho, eliminado = self._eliminar(nodo.derecho, valor)
            return nodo, eliminado

        # Cero o un hijo: la referencia disponible reemplaza al nodo.
        if nodo.izquierdo is None:
            return nodo.derecho, True
        if nodo.derecho is None:
            return nodo.izquierdo, True

        # Dos hijos: copiar el sucesor y retirarlo de su posición original.
        sucesor = self._nodo_minimo(nodo.derecho)
        nodo.dato = sucesor.dato
        nodo.derecho, _ = self._eliminar(nodo.derecho, sucesor.dato)
        return nodo, True


def mostrar_menu() -> None:
    """Presenta las catorce opciones obligatorias."""
    print("\n=== Sistema de operaciones con árbol binario de búsqueda ===")
    print("1. Insertar valor")
    print("2. Buscar valor y mostrar ruta")
    print("3. Ver recorrido inorden")
    print("4. Ver recorrido preorden")
    print("5. Ver recorrido postorden")
    print("6. Ver recorrido por niveles")
    print("7. Ver altura del árbol")
    print("8. Contar nodos")
    print("9. Contar hojas")
    print("10. Mostrar valor mínimo")
    print("11. Mostrar valor máximo")
    print("12. Eliminar valor")
    print("13. Mostrar resumen del árbol")
    print("14. Salir")


def leer_entero(mensaje: str) -> int:
    """Repite la solicitud hasta recibir un número entero válido."""
    while True:
        entrada = input(mensaje).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Entrada no válida. Escriba un número entero.")


def mostrar_recorrido(nombre: str, valores: list[int]) -> None:
    """Imprime un recorrido o avisa si el árbol está vacío."""
    if valores:
        print(f"{nombre}:", " -> ".join(map(str, valores)))
    else:
        print(f"{nombre}: el árbol está vacío.")


def insertar_valor(arbol: ArbolBinarioBusqueda) -> None:
    """Solicita un valor y explica si fue insertado."""
    valor = leer_entero("Valor a insertar: ")
    if arbol.insertar(valor):
        print(f"Valor {valor} insertado correctamente.")
    else:
        print(f"El valor {valor} ya existe; no se permiten duplicados.")


def buscar_valor(arbol: ArbolBinarioBusqueda) -> None:
    """Solicita un valor y muestra la ruta aunque no aparezca."""
    if arbol.esta_vacio():
        print("El árbol está vacío; no hay valores para buscar.")
        return
    valor = leer_entero("Valor a buscar: ")
    encontrado, ruta = arbol.buscar_con_ruta(valor)
    print("Ruta:", " -> ".join(map(str, ruta)))
    if encontrado:
        print(f"Valor {valor} encontrado.")
    else:
        print(f"Valor {valor} no encontrado; la ruta terminó en una rama vacía.")


def mostrar_niveles(arbol: ArbolBinarioBusqueda) -> None:
    """Imprime cada nivel en una línea separada."""
    niveles = arbol.recorrido_por_niveles()
    if not niveles:
        print("Recorrido por niveles: el árbol está vacío.")
        return
    print("Recorrido por niveles:")
    for numero, valores in enumerate(niveles):
        print(f"Nivel {numero}:", " -> ".join(map(str, valores)))


def eliminar_valor(arbol: ArbolBinarioBusqueda) -> None:
    """Elimina, informa el caso y muestra el inorden de validación."""
    if arbol.esta_vacio():
        print("El árbol está vacío; no hay valores para eliminar.")
        return
    valor = leer_entero("Valor a eliminar: ")
    caso = arbol.describir_caso(valor)
    if caso is None:
        print(f"El valor {valor} no existe; no se realizó ninguna eliminación.")
        return
    arbol.eliminar(valor)
    print(f"Valor {valor} eliminado. Caso resuelto: {caso}.")
    mostrar_recorrido("Inorden para validar el BST", arbol.inorden())


def mostrar_extremo(nombre: str, valor: int | None) -> None:
    """Muestra mínimo o máximo y contempla un árbol vacío."""
    if valor is None:
        print(f"{nombre}: el árbol está vacío.")
    else:
        print(f"{nombre}: {valor}")


def mostrar_resumen(arbol: ArbolBinarioBusqueda) -> None:
    """Reúne las principales medidas y el inorden actual."""
    print("\n--- Resumen del árbol ---")
    print("Cantidad de nodos:", arbol.contar_nodos())
    print("Cantidad de hojas:", arbol.contar_hojas())
    print("Altura (en aristas):", arbol.altura())
    mostrar_extremo("Mínimo", arbol.minimo())
    mostrar_extremo("Máximo", arbol.maximo())
    mostrar_recorrido("Recorrido inorden", arbol.inorden())


def cargar_datos_iniciales(arbol: ArbolBinarioBusqueda) -> None:
    """Prepara el caso equilibrado usado en los ejemplos."""
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)


def main() -> None:
    """Ejecuta el menú hasta que el usuario seleccione salir."""
    arbol = ArbolBinarioBusqueda()
    cargar_datos_iniciales(arbol)
    print("Datos iniciales cargados: 50, 30, 70, 20, 40, 60, 80")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            insertar_valor(arbol)
        elif opcion == "2":
            buscar_valor(arbol)
        elif opcion == "3":
            mostrar_recorrido("Inorden", arbol.inorden())
        elif opcion == "4":
            mostrar_recorrido("Preorden", arbol.preorden())
        elif opcion == "5":
            mostrar_recorrido("Postorden", arbol.postorden())
        elif opcion == "6":
            mostrar_niveles(arbol)
        elif opcion == "7":
            print("Altura del árbol (en aristas):", arbol.altura())
        elif opcion == "8":
            print("Cantidad de nodos:", arbol.contar_nodos())
        elif opcion == "9":
            print("Cantidad de hojas:", arbol.contar_hojas())
        elif opcion == "10":
            mostrar_extremo("Valor mínimo", arbol.minimo())
        elif opcion == "11":
            mostrar_extremo("Valor máximo", arbol.maximo())
        elif opcion == "12":
            eliminar_valor(arbol)
        elif opcion == "13":
            mostrar_resumen(arbol)
        elif opcion == "14":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Seleccione un número del 1 al 14.")


if __name__ == "__main__":
    main()
