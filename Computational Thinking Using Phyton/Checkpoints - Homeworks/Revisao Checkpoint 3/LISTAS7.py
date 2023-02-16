'''
Escreva um programa em Python que leia uma matriz M [5x5] e, a cada linha, multiplique cada elemento pelo
valor do elemento inserido na diagonal principal da linha. Os elementos da matriz serão fornecidos pelo usuário.
 Escrever a matriz M lida e a matriz M modificada.
'''

matriz = []

for lin in range(0,5):
    linha = []
    for col in range(0,5):
        num = int(input("Digite um elemento: "))
        linha.append(num)
    matriz.append(linha)
print(matriz)

print("\n\n")
for i in range (0,5):
    print(matriz[i]) #Ver matriz em linhas

for lin in range (0,5):
    diagonal = matriz[lin][lin] #[lin][lin] = lin == lin
    for col in range (0,5):
            matriz[lin][col] =  matriz[lin][col] * diagonal

print("\n\n")
for i in range (0,3):
    print(matriz[i])














