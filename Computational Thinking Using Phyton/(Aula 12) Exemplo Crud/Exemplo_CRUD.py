#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# CRUD - Create, Read, Update, Delete
resp = 1

contatos = {}

while (resp != 0):
    print("1-Incluir ")
    print("2-Alterar ")
    print("3-Exibir ")
    print("4-Excluir ")
    opc = int(input("Digite a opcao desejada: "))
    if (opc==1):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        contatos[nome] = {'nome': nome,'telefone': telefone}
    elif (opc==2):
        nome = input("Nome: ")
        if (nome in contatos):
            contatos[nome]['telefone']=input("Telefone: ")
        else:
            print("Contato não encontrado!")
    elif (opc==3):
        print(contatos)
    elif (opc==4):
        nome = input("Nome: ")
        if (nome in contatos):
            del contatos[nome]
        else:
            print("Contato não encontrado!")
        
    resp = int(input("Deseja continuar (1-SIM / 0-NÃO): "))

