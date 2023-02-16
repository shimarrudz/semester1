'''Escreva um programa em Python para ler duas listas A e B com 10 elementos cada.
 Construir uma lista C, sendo esta a junção das 2 outras listas. Desta forma C deve ter o dobro de
  elementos em relação às listas A e B, ou seja, a lista C deverá possuir 20 elementos. Apresentar a lista C.'''

listaA = []
listaB = []
listaC = []

for i in range(0,10):
    listaA_read = int(input("Digite um número da lista A: "))
    listab_read = int(input("Digite um número da lista B: "))
    listaA.append(listaA_read)
    listaB.append(listab_read)

for i in range(0,10):
    listaA[i]
    listaC.append(listaA[i])

for i in range(0,10):
    listaB[i]
    listaC.append(listaB[i])

print(listaA)
print(listaB)
print(listaC)
