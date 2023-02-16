'''Escreva um programa em Python para ler 12 elementos inteiros para uma lista A. Construir uma lista B
de mesmo tipo e dimensão, observando a seguinte lei de formação: "Todo elemento da lista A que for ímpar deve
ser multiplicado por 2; caso contrário, o elemento da lista A deve permanecer constante". Apresentar a listaB.'''

listaA = []
listaB = []

for i in range(0,12):
    listaA_read = int(input("Digite um número inteiro: "))
    listaA.append(listaA_read)
    listaB.append(listaA_read)

for i in range(0,12):
    if (listaA[i] % 2 != 0):
        listaA[i] *= 2

print(listaA)
print(listaB)



