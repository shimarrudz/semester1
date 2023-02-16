funcionarios = {}

for i in range(0, 2):
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = input("Digite o salário do funcionário: ")
    funcionarios[nome] = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

print(funcionarios)

nome_encontrar = input("Qual funcionário você deseja encontrar? ")
if nome_encontrar in funcionarios:
    funcionario = funcionarios[nome]
    print(funcionario)
else:
    print("Funcionário não encontrado.")