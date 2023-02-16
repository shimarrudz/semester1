'''Escreva um programa em Python que dada uma string com uma frase informada pelo usuário (incluindo espaços em branco),
 conte quantos espaços em branco existem na frase.'''


frase = input("Digite a frase: ")

quant_brancos = 0

##Não faz papel de contador, ele recebe as Strings no index determinado
for letra in frase:
    if (letra == " "):
        quant_brancos += 1

print("Quantidade de espaços em branco ", quant_brancos)

