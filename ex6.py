# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica a faixa do valor da compra para definir o desconto
if valor_compra <= 500:
    desconto = 0.10  # 10%
elif valor_compra <= 1000:
    desconto = 0.15  # 15%
else:
    desconto = 0.20  # 20%

# Calcula o valor do desconto e o valor final a pagar
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
