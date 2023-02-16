matrizA = []

for lin in range (0,3):
    linha = []
    for col in range (0,6):
        linha.append(int(input("Elemento: ")))
    matrizA.append(linha)

listaB = []
for col in range (0,6):
    soma = 0
    for lin in range (0,3):
        if (col % 2 != 0):
            soma+=matrizA[lin][col]
    if (soma != 0):
        listaB.append(soma)

for i in range (0,3):
    print(matrizA[i])
print("\n")

print(listaB)
