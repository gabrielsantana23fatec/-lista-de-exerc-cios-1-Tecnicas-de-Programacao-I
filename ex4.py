# Solicita ao usuário o valor total das vendas do mês
vendas = float(input("Digite o valor total das vendas do mês: R$ "))

# Calcula 5% de comissão sobre as vendas
comissao = vendas * 0.05

# Se as vendas forem acima de R$ 10.000,00, adiciona o bônus de R$ 200,00
if vendas > 10000:
    comissao += 200

# Exibe o valor total da comissão
print(f"\nA comissão total do vendedor é: R$ {comissao:.2f}")
