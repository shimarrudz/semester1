'''§ Escreva um programa em Python que crie uma lista de 10 pets, utilizando o conceito de dicionários, contendo os seguintes dados:

ü Nome;

ü Espécie (cão ou gato);

ü Raça;

ü Porte (pequeno, médio ou grande);

ü Peso.

Depois da lista criada, faça um relatório de cães por raça (deve ser definida pelo usuário), com peso acima de 4 quilos.'''

pets = {}

for i in range (0,2):
    nome = input("Nome: ")
    turno = input("Espécie: ")
    idade = input("Raça: ")
    porte = input("Porte: ")
    peso = input("Peso: ")
    pets[nome] = {"nome": nome,
                    "turno": turno,
                    "idade": idade,
                    "porte": porte,
                    "peso": peso,
                  }



raca = input("Digite a raça desejada: ")

for chave, valor in pets.items():
    if (valor["raça"] == raca and valor["peso"] > 4):
        print(pets[chave])