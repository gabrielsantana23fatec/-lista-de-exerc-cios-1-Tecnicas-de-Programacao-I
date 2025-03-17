while True:
    try:
        numero = float(input("Digite um número positivo: "))
        if numero > 0:
            break  # Encerra o loop se o número for positivo
        else:
            print("Erro: o número deve ser maior que zero. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

print(f"Você digitou o número positivo: {numero}")
