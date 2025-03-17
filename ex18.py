def calcular_media(notas):
    """
    Recebe uma lista de notas e retorna a média aritmética.
    Se a lista estiver vazia, retorna 0.
    """
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Exemplo de uso:
notas_aluno = [7.5, 8.0, 9.0, 6.5]
media = calcular_media(notas_aluno)
print(f"A média das notas é: {media:.2f}")
