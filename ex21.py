# Inicializa a lista de compras
lista_compras = []

while True:
    item = input("Digite um item para adicionar à lista (ou 'sair' para finalizar): ").strip()
    
    if item.lower() == "sair":
        break
    
    lista_compras.append(item)

# Exibe a lista de compras
print("\nLista de Compras:")
for i, item in enumerate(lista_compras, 1):
    print(f"{i}. {item}")
