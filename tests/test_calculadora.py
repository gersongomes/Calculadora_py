import pytest
from app.calculadora import Calculadora

calc = Calculadora()

def test_somar():
    assert calc.somar(2, 3) == 1

def test_subtrair():
    assert calc.subtrair(5, 2) == 3

def test_multiplicar():
    assert calc.multiplicar(3, 4) == 12

def test_dividir():
    assert calc.dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        calc.dividir(10, 0)

def test_potencia():
    assert calc.potencia(2, 3) == 8

def test_raiz_quadrada():
    assert calc.raiz_quadrada(9) == 3

def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-4)
