'''Escreva um programa em Python para ler 15 elementos de uma lista A. Construir uma lista B,
observando a seguinte lei de formação: Todo elemento de B deve ser o quadrado do elemento de A correspondente
. Apresentar as listas A e B.'''

listaA = []
listaB = []

for i in range (0,15):
    num = int(input("Digite um número inteiro: "))
    listaA.append(num)

for i in range (0,15):
    quadrado = listaA[i] * listaA[i]
    listaB.append(quadrado)

print(listaA)
print(listaB)
