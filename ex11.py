# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))

# Números menores que 2 não são considerados primos
if numero < 2:
    print(f"{numero} não é primo.")
else:
    # Assume que o número é primo até que se prove o contrário
    primo = True
    # Verifica divisores de 2 até a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    # Exibe o resultado
    if primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
