def calculadora(a, b, operacao):
    """
    Função que realiza operações matemáticas básicas.
    :param a: Primeiro número
    :param b: Segundo número
    :param operacao: Operação desejada ('+', '-', '*', '/')
    :return: Resultado da operação ou mensagem de erro se a operação for inválida
    """
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    else:
        return "Erro: Operação inválida"

# Exemplo de uso
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

resultado = calculadora(a, b, operacao)
print("Resultado:", resultado)
