lista_notas = []
soma = 0
quant_valoresacimamedia = 0
quant_valoresbaixo7 = 0

nota = float(input("Digite o valor da nota: "))

while(nota != -1):
    lista_notas.append(nota)
    nota = float(input("Digite o valor da nota: "))

tam_lista = len(lista_notas)

for i in range(0,tam_lista):
    soma = soma + lista_notas[i]
    if (lista_notas[i] < 7.0):
        quant_valoresbaixo7 += 1

media = soma / tam_lista

for i in range(0,tam_lista):
    if (lista_notas[i] > media):
        quant_valoresacimamedia += 1

print("Quantidade de notas da lista ", tam_lista)
print(f"Soma das notas:  {soma:.2f}")
print(f"Média da notas: {media:.2f}")
print("Quantidade de valores acima da média calculada: ", quant_valoresacimamedia)
print("Quantidade de valores abaixo da média: ",quant_valoresbaixo7)
