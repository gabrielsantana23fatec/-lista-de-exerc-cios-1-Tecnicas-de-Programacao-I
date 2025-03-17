# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Define as vogais (em minúsculas e maiúsculas, para maior abrangência)
vogais = "aeiouAEIOU"

# Inicializa o contador de vogais
contador = 0

# Percorre cada letra da palavra e verifica se é uma vogal
for letra in palavra:
    if letra in vogais:
        contador += 1

# Exibe o número de vogais encontradas
print(f"Número de vogais na palavra '{palavra}': {contador}")
