'''Crie um programa que recebe uma string e um caractere digitados pelo usuário e retorne o número de vezes que esse caractere aparece na string.'''

palavra = input("Digite uma palavra com 0´s e 1´s ")
caracteres = input("Digite o caractere que deseja saber a quantidade: ")

quant_caracteres = 0

for letra in palavra:
    if (letra == caracteres):
        quant_caracteres += 1

print("Quantidade de caracteres ", caracteres, "na string é: ", quant_caracteres)
