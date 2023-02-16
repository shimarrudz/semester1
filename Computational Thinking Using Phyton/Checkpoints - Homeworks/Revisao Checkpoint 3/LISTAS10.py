'''Faça um programa em Python que conte o número de 1’s que aparecem em uma string. Exemplo: “0011001” = 3.'''

palavra = input("Digite uma palavra com 0´s e 1´s ")

quant_uns = 0

for letra in palavra:
    if (letra == "1"):
        quant_uns += 1

print("Quantidade de uns na string: ", quant_uns)
