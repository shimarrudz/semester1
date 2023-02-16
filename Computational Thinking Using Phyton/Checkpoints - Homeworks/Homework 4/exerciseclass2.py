salario = float(input("Digite o salário: "))

if salario >= 800:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.20

print(f"Novo salário: {novo_salario:.2f}")
