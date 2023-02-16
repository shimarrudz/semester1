matriz = []

for lin in range (0,3):
    linha = []
    for col in range (0,3):
        num = int(input("Digite um elemento: "))
        linha.append(num)
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]
lin_maior = 0
col_maior = 0
lin_maior = 0
col_menor = 0

for i in range (0,6):
    for col in range (0,3):
        if (matriz[lin][col] > maior):
            maior = matriz[lin][col]
            lin_maior = lin
            col_maior = col
        if (matriz[lin][col] > maior):
            maior = matriz[lin][col]
            lin_menor = lin
            col_menor = col

for i in range (0,6):
    print(matriz[i])

print("O maior elemento é ", maior, "está na linha ", lin_maior," e coluna ", col_maior)
print("O menor elemento é ", menor, "está na linha", lin_menor, "e coluna", lin_menor)
