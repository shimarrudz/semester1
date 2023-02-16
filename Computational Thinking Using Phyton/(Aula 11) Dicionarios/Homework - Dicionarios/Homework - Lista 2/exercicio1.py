resp = 1

clientes = {}

while (resp != 0):
    print("1-Incluir ")
    print("2-Alterar ")
    print("3-Exibir ")
    print("4-Excluir ")
    opcao = int(input("Digite a opção desejada: "))
    if (opcao == 1):
        nome = input("Nome: ")
        telefone = int(input("CPF: "))
        idade = int(input("Idade: "))
        endereco = input("Digite o endereço")
        limite_credito = float(input("Digite o limite de saldo: "))
        clientes[nome] = {"nome": nome,
                          "telefone": telefone,
                          "idade": idade,
                          "endereco": endereco,
                          "limite": limite_credito}
    elif (opcao == 2):
        nome = input("Nome: ")
        if (nome in clientes):
            clientes[nome]["CPF"]= input("CPF: ")
            clientes[nome]["Idade"]= int(input("Idade: "))
            clientes[nome]["Digite o endereço"] = input("Idade: ")
            clientes[nome]["Limite de credito:"] = float(input("Limite de credito:: "))
        else:
            print("Contato não encontrado!")
    elif (opcao == 3):
        print(clientes)
    elif (opcao == 4):
        nome = input("Nome: ")
        if (nome in clientes):
            del clientes[nome]
        else:
            print("Contato não encontrado!")

    resp = int(input("deseja continuar (1-SIM / 0-NÃO "))

print(clientes)