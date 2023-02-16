resp = 1

funcionarios = {}

while (resp != 0):
    print("1-Incluir ")
    print("2-Alterar ")
    print("3-Exibir ")
    print("4-Excluir ")
    opc = int(input("Digite a opcao desejada: "))
    if (opc == 1):
        nome = input("Nome: ")
        cpf = input("Cpf: ")
        lista_data_nasc = []
        lista_data_nasc.append(int(input("Dia de nasc: ")))
        lista_data_nasc.append(int(input("Mês de nasc: ")))
        lista_data_nasc.append(int(input("Ano de nasc: ")))
        cargo = input("Cargo: ")
        salario_bruto = float(input("Salário bruto: "))
        desc_INSS = salario_bruto * 0.15
        desc_IR = salario_bruto * 0.1895
        salario_liquido = salario_bruto - desc_INSS - desc_IR
        funcionarios[nome] = {'nome': nome, 'cpf': cpf, 'data_nasc': lista_data_nasc, 'cargo': cargo,
                              'salario_bruto': salario_bruto, 'desc_INSS': desc_INSS,
                              'desc_IR': desc_IR, 'salario_liquido': salario_liquido}
    elif (opc == 2):
        nome = input("Nome: ")
        if (nome in funcionarios):
            funcionarios[nome]['cpf'] = input("Cpf: ")
            lista_data_nasc = []
            lista_data_nasc.append(int(input("Dia de nasc: ")))
            lista_data_nasc.append(int(input("Mês de nasc: ")))
            lista_data_nasc.append(int(input("Ano de nasc: ")))
            funcionarios[nome]['data_nasc'] = lista_data_nasc
            funcionarios[nome]['cargo'] = input("Cargo: ")
            funcionarios[nome]['salario_bruto'] = float(input("Salário bruto: "))
            funcionarios[nome]['desc_INSS'] = funcionarios[nome]['salario_bruto'] * 0.15
            funcionarios[nome]['desc_IR'] = funcionarios[nome]['salario_bruto'] * 0.1895
            funcionarios[nome]['salario_liquido'] = funcionarios[nome]['salario_bruto'] - funcionarios[nome]['desc_INSS'] - funcionarios[nome]['desc_IR']
        else:
            print("Funcionário não encontrado!")
    elif (opc == 3):
        print(funcionarios)
    elif (opc == 4):
        nome = input("Nome: ")
        if (nome in funcionarios):
            del funcionarios[nome]
        else:
            print("Funcionário não encontrado!")

    resp = int(input("Deseja continuar (1-SIM / 0-NÃO): "))

soma_salarios = 0
for chave, subdic in funcionarios.items():
    print(subdic)
    soma_salarios+=subdic['salario_bruto']

print(f"Soma dos salários brutos: {soma_salarios:.2f}")

print("\n")

for chave, subdic in funcionarios.items():
    if (subdic['cargo'] == "Desenvolvedor frontend" and subdic['salario_bruto'] > 5000):
        print(subdic)

print("\n")

for chave, subdic in funcionarios.items():
    if (subdic['data_nasc'][2] == 1998 and subdic['salario_liquido'] > 3200):
        print(subdic)
