from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from soluciones.practica_busquedas_solucion import (  # noqa: E402
    busqueda_binaria,
    busqueda_lineal,
)


CODIGOS = [1001, 1005, 1010, 1020, 1035, 1040, 1055, 1060, 1075, 1080]


def test_busqueda_lineal_encontrado_al_inicio() -> None:
    assert busqueda_lineal(CODIGOS, 1001) == (0, 1)


def test_busqueda_lineal_encontrado_cerca_del_final() -> None:
    assert busqueda_lineal(CODIGOS, 1055) == (6, 7)


def test_busqueda_lineal_no_encontrado() -> None:
    assert busqueda_lineal(CODIGOS, 1099) == (-1, 10)


def test_busqueda_binaria_encontrado_al_inicio() -> None:
    assert busqueda_binaria(CODIGOS, 1001) == (0, 3)


def test_busqueda_binaria_encontrado_cerca_del_final() -> None:
    assert busqueda_binaria(CODIGOS, 1055) == (6, 4)


def test_busqueda_binaria_no_encontrado() -> None:
    assert busqueda_binaria(CODIGOS, 1099) == (-1, 4)
