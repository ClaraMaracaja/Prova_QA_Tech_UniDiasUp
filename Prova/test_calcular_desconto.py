import pytest
from calcular_desconto import calcular_desconto  # ajuste o import ao seu projeto


@pytest.mark.parametrize("valor, tipo, esperado", [
    (50, "COMUM", 0),
    (99.99, "COMUM", 0),
    (100, "COMUM", 10),
    (300, "COMUM", 30),
    (499.99, "COMUM", 50.0),
    (500, "COMUM", 100),
    (50, "VIP", 2.5),
    (100, "VIP", 15),
    (300, "VIP", 45),
    (500, "VIP", 125),
])
def test_faixas_de_desconto(valor, tipo, esperado):
    assert calcular_desconto(valor, tipo) == pytest.approx(esperado)


@pytest.mark.parametrize("tipo", ["vip", "Vip", "vIP", " vip "])
def test_vip_ignora_maiusculas_e_minusculas(tipo):
    assert calcular_desconto(300, tipo) == pytest.approx(45)


def test_comum_em_minusculo():
    assert calcular_desconto(300, "comum") == pytest.approx(30)


@pytest.mark.parametrize("valor, tipo", [
    (1000, "COMUM"),
    (1500, "COMUM"),
    (800, "VIP"),
    (1000, "VIP"),
])
def test_teto_de_200_reais(valor, tipo):
    assert calcular_desconto(valor, tipo) == 200


def test_compra_zerada():
    assert calcular_desconto(0, "COMUM") == 0


@pytest.mark.parametrize("valor", [-100, "abc", None])
def test_valor_invalido_lanca_erro(valor):
    with pytest.raises(ValueError):
        calcular_desconto(valor, "COMUM")


@pytest.mark.parametrize("tipo", ["GOLD", "", None])
def test_tipo_cliente_invalido_lanca_erro(tipo):
    with pytest.raises(ValueError):
        calcular_desconto(100, tipo)