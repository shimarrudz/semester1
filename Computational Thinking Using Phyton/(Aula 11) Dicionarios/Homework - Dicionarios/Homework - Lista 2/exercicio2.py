estoque = {}

resp = 1

while(resp != 0):
    print("1-Incluir ")
    print("2-Alterar ")
    print("3-Exibir ")
    print("4-Excluir ")
    opcao = int(input("Digite a opção desejada: "))
    if (opcao == 1):
        descricao = input("Descrição: ")
        quantidade = int(input("Quantidade: "))
        marca = input("Marca: ")
        valor = float(input("Valor: "))
        estoque[descricao] = {"descricao": descricao,
                          "quantidade": quantidade,
                          "marca": marca,
                          "valor":valor,}
    elif (opcao == 2):
        descricao = input("Descrição: ")
        if (descricao in estoque):
            estoque[descricao]["quantidade"] = int(input("Quantidade: "))
            estoque[descricao]["marca"] = input("Marca: ")
            estoque[descricao]["valor"] = input("Valor: ")
        else:
            print("Produto não encontrado! ")
    elif (opcao == 3):
        print(estoque)
    elif (opcao == 4):
        descricao = input("Descrição: ")
        if (descricao in estoque):
            del estoque[descricao]
        else:
            print("Contato não encontrado!")
    resp = int(input("Deseja continuar (1-SIM / 0-NÃO): "))

marca = input("Digite a marca que deseja ver o relatorio: ")
for chave, valor in estoque.items():
    if (valor["marca"] == marca and valor["quantidade"] > 50):
        print(estoque[chave])

