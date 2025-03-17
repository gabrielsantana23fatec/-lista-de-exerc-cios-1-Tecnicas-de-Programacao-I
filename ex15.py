while True:
    print("\nMenu:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("Você escolheu a Opção 1.")
        # Insira a lógica para a Opção 1 aqui.
    elif escolha == "2":
        print("Você escolheu a Opção 2.")
        # Insira a lógica para a Opção 2 aqui.
    elif escolha == "3":
        print("Você escolheu a Opção 3.")
        # Insira a lógica para a Opção 3 aqui.
    elif escolha == "4":
        print("Saindo do menu. Até logo!")
        break  # Encerra o loop e sai do programa.
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
