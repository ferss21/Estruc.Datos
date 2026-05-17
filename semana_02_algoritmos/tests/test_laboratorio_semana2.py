from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from soluciones.laboratorio_semana2_solucion import (  # noqa: E402
    analizar_numeros,
    calcular_promedio,
    calcular_suma,
    contar_positivos,
    obtener_mayor,
)


def test_calcular_suma() -> None:
    assert calcular_suma([2, -1, 5]) == 6


def test_contar_positivos() -> None:
    assert contar_positivos([2, -1, 0, 5]) == 2


def test_obtener_mayor() -> None:
    assert obtener_mayor([2, -1, 10, 5]) == 10
    assert obtener_mayor([]) is None


def test_calcular_promedio() -> None:
    assert calcular_promedio([10, 20, 30]) == 20
    assert calcular_promedio([]) == 0


def test_analizar_numeros() -> None:
    resultado = analizar_numeros([12, -4, 7, 0, 25, -10, 8])

    assert resultado["suma"] == 38
    assert resultado["positivos"] == 4
    assert resultado["mayor"] == 25
    assert resultado["promedio"] == 38 / 7
    assert resultado["operaciones"] == 7
    assert resultado["tiempo"] >= 0
