lista_1 = []
lista_2 = []
lista_intercalada = []

for i in range (0,10):
    num1 = int(input("Digite um número: "))
    lista_1.append(num1)
    num2 = int(input("Digite um número: "))
    lista_2.append(num2)

for i in range (0,10):
    lista_intercalada.append(lista_1[i])
    lista_intercalada.append(lista_2[i])

print(lista_1)
print(lista_2)
print(lista_intercalada)

