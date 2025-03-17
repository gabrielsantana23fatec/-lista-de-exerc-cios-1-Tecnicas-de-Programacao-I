# Solicita 3 notas do usuário e armazena em uma lista
notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Calcula a média das notas
media = sum(notas) / len(notas)

# Exibe a média
print(f"A média das notas é: {media:.2f}")
