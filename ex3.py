# Solicita ao usuário o número de vitórias, empates e derrotas
vitorias = int(input("Digite o número de vitórias: "))
empates = int(input("Digite o número de empates: "))
derrotas = int(input("Digite o número de derrotas: "))

# Calcula a pontuação total
pontuacao_total = (vitorias * 10) + (empates * 5) + (derrotas * 0)

# Exibe o resultado
print(f"\nPontuação total do jogador: {pontuacao_total} pontos")
