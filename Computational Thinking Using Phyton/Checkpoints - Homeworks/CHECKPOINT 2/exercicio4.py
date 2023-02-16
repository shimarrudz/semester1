
soma_pares = 0
for i in range(1,11):
    num = int(input("Digite um número: "))
    if (num % 2 == 0):
        soma_pares += num

print("Soma dos pares: ", soma_pares)