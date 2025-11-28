
import pytest

from app.validator import dividir

def test_division_exitosa_enteros():
    assert dividir(10, 5) == 2

def test_division_por_cero():
    with pytest.raises(Exception) as excinfo:
        dividir(10, 0)
    assert str(excinfo.value) == "No se puede dividir por cero"

@pytest.mark.parametrize("dividendo, divisor", [
    (-10, 5),    # Dividendo negativo
    (10, -5),    # Divisor negativo
    (-10, -5)    # Ambos negativos
])
def test_numeros_negativos(dividendo, divisor):
    with pytest.raises(Exception) as excinfo:
        dividir(dividendo, divisor)
    assert str(excinfo.value) == "Los numeros deben ser positivos"
