# Dicionário com traduções básicas
tradutor = {
    "gato": "cat",
    "cachorro": "dog",
    "livro": "book",
    "computador": "computer",
    "mesa": "table",
    "cadeira": "chair",
    "carro": "car",
    "janela": "window"
}

while True:
    palavra = input("Digite uma palavra para traduzir (ou 'sair' para finalizar): ").strip().lower()
    
    if palavra == "sair":
        break
    
    if palavra in tradutor:
        print(f"A tradução de '{palavra}' é: {tradutor[palavra]}")
    else:
        print("Palavra não encontrada no dicionário.")
