'''Escreva um programa em Python para ler uma lista A com 10 elementos numéricos inteiros.
 Apresentar o total de elementos ímpares existentes na lista e o percentual
do valor total de números ímpares em relação à quantidade total de elementos armazenados na lista.'''

listaA = []
lista_impares = 0

for i in range(0,10):
    num = int(input("Digite um número inteiro: "))
    listaA.append(num)

for i in range (0,10):
    if (listaA[i] % 2 != 0):
        lista_impares += 1


tamlista = len(listaA)

percentual = (lista_impares * 100) / tamlista

print(listaA)
print(lista_impares)
print(f"O percentual dos elementos da lista de impares é de: {percentual:.2f} %")
