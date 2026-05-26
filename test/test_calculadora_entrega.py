import pytest
from src.calculadora_entrega import calcular_taxa_entrega

def test_ate_3km():
    distancia = 2
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 5.0

def test_acima_de_3km():
    distancia = 5
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 9.0

def test_distancia_negativa():
    distancia = -1
    with pytest.raises(ValueError, match="Distância não pode ser negativa"):
        calcular_taxa_entrega(distancia)