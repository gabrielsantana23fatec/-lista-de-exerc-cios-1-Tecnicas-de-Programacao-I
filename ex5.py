# Solicita ao usuário o salário bruto
salario_bruto = float(input("Digite o salário bruto do funcionário: R$ "))

# Calcula o desconto do INSS (10%)
desconto_inss = salario_bruto * 0.10

# Calcula o desconto do Imposto de Renda (IR) de acordo com a faixa salarial
if salario_bruto <= 2000:
    desconto_ir = 0
elif salario_bruto <= 5000:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20

# Calcula o salário líquido
salario_liquido = salario_bruto - desconto_inss - desconto_ir

# Exibe os resultados
print(f"\nSalário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (10%): R$ {desconto_inss:.2f}")
print(f"Desconto IR: R$ {desconto_ir:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
