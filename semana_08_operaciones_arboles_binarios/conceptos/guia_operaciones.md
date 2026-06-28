# Guía de operaciones en árboles binarios de búsqueda

## ¿Qué significa operar un árbol?

Operar un árbol significa consultar o modificar sus nodos siguiendo reglas definidas. En un árbol binario de búsqueda, todo valor del subárbol izquierdo es menor que el nodo y todo valor del subárbol derecho es mayor. Esa regla permite descartar una rama completa en cada comparación.

## Insertar

Insertar consiste en encontrar un espacio vacío para un valor nuevo. Se empieza en la raíz: si el valor es menor se avanza a la izquierda; si es mayor, a la derecha. El proceso se repite hasta hallar una referencia vacía. En este material los duplicados no se insertan porque no aportan una posición única.

Ejemplo al insertar `65`: `50 -> 70 -> 60 -> derecha`. El 65 es mayor que 50, menor que 70 y mayor que 60.

## Buscar y mostrar la ruta

Buscar usa las mismas comparaciones que insertar, pero no modifica el árbol. La ruta de búsqueda es la secuencia de nodos visitados. Si se llega al valor, la búsqueda termina con éxito; si se llega a una rama vacía, el valor no existe.

Buscar no es lo mismo que recorrer. Buscar intenta visitar una sola ruta. Recorrer visita todos los nodos en un orden determinado.

## Medir altura y profundidad

La **altura** de un nodo es la mayor cantidad de aristas desde ese nodo hasta una hoja. La altura del árbol es la altura de su raíz. Con la convención utilizada aquí, una hoja tiene altura 0 y un árbol vacío tiene altura -1.

La **profundidad** indica cuántas aristas separan la raíz de un valor. La raíz tiene profundidad 0. Si el valor no existe, el programa puede devolver `None` y mostrar un mensaje claro.

## Contar nodos

Para contar nodos se suma uno por el nodo actual y luego se cuentan sus subárboles:

`total = 1 + nodos de la izquierda + nodos de la derecha`

El árbol vacío contiene cero nodos. El conteo sirve para comprobar inserciones y eliminaciones.

## Contar hojas

Una hoja es un nodo sin hijo izquierdo ni derecho. Si un nodo es hoja, aporta uno al conteo. Los nodos internos no se cuentan como hojas, aunque tengan solamente un hijo.

## Recorrido por niveles

El recorrido por niveles visita primero la raíz, luego sus hijos, después los nietos y así sucesivamente. Utiliza una cola: se retira el primer nodo pendiente y se agregan sus hijos al final. También se conoce como recorrido en anchura.

## Mínimo y máximo en un BST

El mínimo está en el extremo izquierdo porque cada paso a la izquierda conduce a un valor menor. El máximo está en el extremo derecho. Si el árbol está vacío, ninguno de los dos existe y el programa debe manejar ese caso.

## Recorridos en profundidad

- **Preorden:** raíz, izquierda, derecha. Es útil para observar primero cada raíz.
- **Inorden:** izquierda, raíz, derecha. En un BST produce valores ordenados.
- **Postorden:** izquierda, derecha, raíz. Procesa los hijos antes que su padre.

## ¿Por qué eliminar es más complejo?

Al insertar se ocupa una referencia vacía. Al eliminar, en cambio, hay que reconectar las ramas sin romper la regla del BST. La acción depende de la cantidad de hijos del nodo.

### Caso 1: eliminar una hoja

Una hoja no sostiene otros nodos. La referencia de su padre se reemplaza por una referencia vacía.

### Caso 2: eliminar un nodo con un hijo

El único hijo ocupa el lugar del nodo eliminado. Así se conserva todo el subárbol que dependía de él.

### Caso 3: eliminar un nodo con dos hijos

No se puede descartar ninguno de los dos subárboles. Una solución común consiste en reemplazar el dato por su sucesor inorden y luego eliminar ese sucesor de su posición original.

## Sucesor inorden

El sucesor inorden es el valor que aparecería inmediatamente después de un nodo en el recorrido inorden. Para un nodo con hijo derecho, es el menor valor de ese subárbol derecho: se avanza una vez a la derecha y luego todo lo posible a la izquierda.

## Árbol balanceado y desbalanceado

Un árbol está razonablemente balanceado cuando sus ramas tienen alturas parecidas. En ese caso, cada comparación descarta muchos valores. Un árbol se desbalancea cuando una rama crece mucho más que las demás. Si se insertan valores ya ordenados, puede adoptar forma de lista y las operaciones dejan de aprovechar bien la estructura.

El balance no depende de que el dibujo sea perfectamente simétrico. Lo importante es que la altura no crezca innecesariamente respecto de la cantidad de nodos.

## Comprobaciones útiles

Después de cada operación conviene verificar:

1. El recorrido inorden sigue ordenado y sin duplicados.
2. La cantidad de nodos cambió solamente cuando correspondía.
3. Buscar el valor insertado funciona.
4. Buscar el valor eliminado informa que ya no existe.
5. Las ramas que no participaron en la operación se conservan.

