matriz = []

for lin in range (0,3):
    linha = []
    for col in range (0,3):
        num = int(input("Digite um elemento: "))
        linha.append(num)
    matriz.append(linha)

for lin in range(0,3):
    soma = 0
    for col in range(0,3):
        soma += matriz[lin][col]
    if (lin == 0):
        maior = soma
        lin_maior = 0
    else:
        if (soma > maior):
            maior = soma
            lin_maior = lin

for i in range (0,3):
    print(matriz[i])

print("\n")
print(matriz[lin_maior])
print("Maior soma: ", maior)