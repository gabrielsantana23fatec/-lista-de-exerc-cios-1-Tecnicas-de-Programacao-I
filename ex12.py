import random

# O programa escolhe um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Inicializa a variável para armazenar o palpite do usuário
palpite = 0

# Loop que continua até o usuário acertar o número
while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
    else:
        print("Errou! Tente novamente.")
