# Cria uma lista com números de 1 a 10
numeros = list(range(1, 11))

# Filtra apenas os números pares
pares = [num for num in numeros if num % 2 == 0]

# Exibe os números pares
print("Números pares:", pares)
