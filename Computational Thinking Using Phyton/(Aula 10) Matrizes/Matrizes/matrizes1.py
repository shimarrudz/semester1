matriz = []
quant_valoresmaiores10 = 0

for lin in range (0, 4):
    linha = []
    for col in range (0,4):
        num = int(input("Digite um elemento: "))
        linha.append(num)
    matriz.append(linha)

for lin in range (0,4):
    for col in range (0,4):
        if (matriz[lin][col] > 10):
            quant_valoresmaiores10 += 1

print(matriz)
print("Quantidade de valores maiores que 10: ")
