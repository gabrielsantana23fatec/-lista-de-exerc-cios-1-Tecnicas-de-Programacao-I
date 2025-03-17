# Solicita o preço do produto e o número de parcelas ao usuário
preco_produto = float(input("Digite o preço do produto: R$ "))
num_parcelas = int(input("Digite o número de parcelas: "))

# Aplica 10% de juros sobre o valor do produto
valor_total = preco_produto * 1.10

# Calcula o valor de cada parcela
valor_parcela = valor_total / num_parcelas

# Exibe os resultados formatados
print(f"\nValor total com juros: R$ {valor_total:.2f}")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
