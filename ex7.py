# Solicita ao usuário que informe um número
numero = int(input("Digite um número para ver a sua tabuada: "))

#mostra atabuada 1 a 10
print(f"\nTabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")