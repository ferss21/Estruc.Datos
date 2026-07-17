# Semana 10 - Tablas Hash y Resolución de Colisiones

## Descripción

Esta semana estudia cómo una tabla hash transforma una clave en un índice para guardar y buscar datos rápidamente. Los ejemplos usan códigos de estudiantes y presentan formas sencillas de reconocer y resolver colisiones.

## Objetivos

- Comprender qué es una tabla hash.
- Calcular índices usando una función hash.
- Identificar colisiones.
- Resolver colisiones con encadenamiento.
- Comprender linear probing.
- Calcular factor de carga.
- Relacionar tablas hash con `dict` y `set`.

## Estructura de carpetas

- `ejemplos`: diez programas independientes sobre funciones hash, colisiones y búsquedas.
- `practica_clase`: sistema de búsqueda de estudiantes mediante una tabla hash con encadenamiento.

```text
semana_10_tablas_hash/
├── README.md
├── ejemplos/
│   ├── 01_funcion_hash.py
│   ├── 02_indice_hash.py
│   ├── 03_colisiones.py
│   ├── 04_encadenamiento.py
│   ├── 05_buscar_encadenamiento.py
│   ├── 06_linear_probing.py
│   ├── 07_factor_carga.py
│   ├── 08_rehashing.py
│   ├── 09_dict_y_set_hash.py
│   └── 10_comparar_busqueda.py
└── practica_clase/
    └── main.py
```

## Comandos de ejecución

```bash
cd semana_10_tablas_hash
python ejemplos/01_funcion_hash.py
python ejemplos/02_indice_hash.py
python ejemplos/03_colisiones.py
python ejemplos/04_encadenamiento.py
python ejemplos/05_buscar_encadenamiento.py
python ejemplos/06_linear_probing.py
python ejemplos/07_factor_carga.py
python ejemplos/08_rehashing.py
python ejemplos/09_dict_y_set_hash.py
python ejemplos/10_comparar_busqueda.py
python practica_clase/main.py
```

## Conceptos clave

La función hash calcula una posición a partir de una clave. Cuando dos claves producen el mismo índice ocurre una colisión. El encadenamiento guarda varios elementos en una lista interna, mientras que *linear probing* busca la siguiente posición disponible. El factor de carga ayuda a reconocer cuándo la tabla comienza a llenarse y conviene aumentar su tamaño.
