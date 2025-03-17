# Solicita ao usuário a quantidade inicial do produto, a quantidade vendida e a quantidade recebida
quantidade_inicial = int(input("Digite a quantidade inicial do produto: "))
quantidade_vendida = int(input("Digite a quantidade vendida: "))
quantidade_recebida = int(input("Digite a quantidade recebida: "))

# Calcula a quantidade final em estoque
quantidade_final = quantidade_inicial - quantidade_vendida + quantidade_recebida

# Exibe o resultado
print(f"\nQuantidade final em estoque: {quantidade_final}")
