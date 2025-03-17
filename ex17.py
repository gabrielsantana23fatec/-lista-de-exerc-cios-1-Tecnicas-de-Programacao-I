def eh_par(numero):
    """Retorna True se o número for par e False se for ímpar."""
    return numero % 2 == 0

# Exemplo de uso:
numero_teste = int(input("Digite um número: "))
if eh_par(numero_teste):
    print(f"{numero_teste} é par.")
else:
    print(f"{numero_teste} é ímpar.")
