def calcular_desconto(valor_compra, tipo_cliente):
    if isinstance(valor_compra, bool) or not isinstance(valor_compra, (int, float)):
        raise ValueError("Valor da compra deve ser numérico")
    if valor_compra < 0:
        raise ValueError("Valor da compra não pode ser negativo")
    if not isinstance(tipo_cliente, str):
        raise ValueError("Tipo de cliente inválido")

    tipo = tipo_cliente.strip().upper()
    if tipo not in ("VIP", "COMUM"):
        raise ValueError("Tipo de cliente inválido")

    if valor_compra >= 500:
        desconto = 0.20
    elif valor_compra >= 100:
        desconto = 0.10
    else:
        desconto = 0

    if tipo == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

    if valor_desconto > 200:
        valor_desconto = 200

    return round(valor_desconto, 2)