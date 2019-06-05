import calculadora
import pytest

@pytest.mark.skip(reason="i dont want to check now")
def test_calc_total():
    total=calculadora.calc_total(1,2)
    assert total==3

def test_calc_multi():
    total=calculadora.calc_multiply(1,2)
    assert total==2
