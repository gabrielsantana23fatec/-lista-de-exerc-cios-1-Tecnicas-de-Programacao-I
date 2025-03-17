# Inicializa o dicionário de contatos
contatos = {}

while True:
    opcao = input("\nDigite '1' para adicionar contato, '2' para buscar, ou 'sair' para finalizar: ").strip()

    if opcao == "1":
        nome = input("Nome do contato: ").strip()
        telefone = input("Número de telefone: ").strip()
        contatos[nome] = telefone
        print(f"Contato {nome} adicionado!")

    elif opcao == "2":
        nome = input("Digite o nome do contato para buscar: ").strip()
        if nome in contatos:
            print(f"Telefone de {nome}: {contatos[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao.lower() == "sair":
        break

    else:
        print("Opção inválida! Tente novamente.")

# Exibe todos os contatos cadastrados
print("\nLista de Contatos:")
for nome, telefone in contatos.items():
    print(f"{nome}: {telefone}")
