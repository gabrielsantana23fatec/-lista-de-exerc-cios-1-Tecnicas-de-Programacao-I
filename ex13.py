import random

# O programa escolhe um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)
tentativas = 0

# Loop que continua até o usuário acertar o número
while True:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1  # Incrementa o contador de tentativas a cada palpite
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou após {tentativas} tentativas!")
        break
    else:
        print("Errou! Tente novamente.")
