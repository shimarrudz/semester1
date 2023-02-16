'''Construa um programa em Python para preencher uma matriz, de 6 linhas por 6 colunas, com elementos
 do tipo int.  Em seguida, o programa deve apresentar, na tela, todos os elementos pares contidos na matriz,
  bem como a posição em que eles se encontram.'''

matriz = []

for lin in range(0,6):
    linha = []
    for col in range(0,6):
        num = int(input("Digite um elemento: "))
        linha.append(num)
    matriz.append(linha)
print(matriz)

for lin in range(0,6):
    for col in range(0,6):
        if (matriz[lin][col] % 2 == 0):
            print("O elemento é ", matriz[lin] [col], "e está na linha ", lin, "e coluna ", col)