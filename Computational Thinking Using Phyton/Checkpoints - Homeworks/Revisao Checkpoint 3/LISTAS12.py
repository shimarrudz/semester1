'''Escreva um programa em Python que crie uma lista (dicionário de dicionários) de 10 alunos de uma academia,
utilizando o conceito de dicionários, contendo os seguintes dados:

ü Nome;

ü Turno (manhã, tarde ou noite);

ü Idade;

ü Peso;

ü Altura;

ü IMC (deve ser calculado como “imc = peso / altura*altura”).

Depois da lista criada, faça um relatório dos alunos que estão com o imc acima do ideal (maior do que 24.9).'''

alunos = {}

for i in range (0,2):
    nome = input("Nome: ")
    turno = input("Turno: ")
    idade = input("idade: ")
    peso = input("Peso ")
    altura = float(input("Altura"))
    imc = peso / altura ** 2
    alunos[nome] = {"nome": nome,
                    "turno": turno,
                    "idade": idade,
                    "peso": peso,
                    "altura": altura,
                    "imc": imc}

for chave, valor in alunos.items():
    if (valor["imc"] > 24.9):
        print(alunos[chave])