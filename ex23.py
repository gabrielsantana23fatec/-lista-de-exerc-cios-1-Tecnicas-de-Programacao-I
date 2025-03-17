# Inicializa o dicionário de alunos e notas
alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ").strip()
    
    if nome.lower() == "sair":
        break
    
    notas = input(f"Digite as notas de {nome}, separadas por espaço: ").strip().split()
    notas = [float(nota) for nota in notas]  # Converte para float
    
    alunos[nome] = notas

# Exibe a lista de alunos e suas médias
print("\nNotas dos Alunos:")
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome}: Notas: {notas} | Média: {media:.2f}")
