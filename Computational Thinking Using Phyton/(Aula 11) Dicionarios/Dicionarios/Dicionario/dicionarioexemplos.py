##Forma de criar dicionário
pessoa = {"nome":"Jõao", "idade":25, "altura": 1.65 }
print(print(type(pessoa)))
print("\n")
print(pessoa)

##Outra forma de criação de dicionário
teste = dict(nome = "Jõao", idade = 25)


print(teste)

#Printa o valor da key
print(pessoa["nome"])

#Printa o valor da key
print(pessoa.get("nome"))

##Mostra as keys
print(pessoa.keys())

##Mostra os valores
print(pessoa.values())

##Adicionar textos
for chave, valor in pessoa.items():
    print("Chave: ", chave, "- Valor", valor)


##Mudar valor de uma key
pessoa["peso"] = 56
print(pessoa)

pessoa.update({"nome":"Pedro"})
print(pessoa)

##Deletar uma key
##del pessoa["peso"]

##Limpar um dicionário
pessoa.clear()

##Preenchimento de dicionário
contatos = {}
for i in range (0,3):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos[nome] = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

print(contatos)
print(contatos["Jõao"])
print(contatos["Ana"])


##Para conferir se o contato está na key do dicionário
nome = input("Nome: ")
if nome in contatos:
        contato = contatos[nome]
        print(contato)
else:
    print("Contato não encontrado")


teste = {"matriz": [[3,5,6], [7,8,9]]}
print(teste["matriz"[1]])

