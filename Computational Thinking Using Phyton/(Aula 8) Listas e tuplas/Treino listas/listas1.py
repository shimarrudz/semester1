lista_geral = []
lista_par = []
lista_impar = []

for i in range(0,10):
    num = int(input("Digite um número: "))
    lista_geral.append(num)

for i in range(0,10):
    if (lista_geral[i] % 2 == 0):
        lista_par.append(lista_geral[i])
    else:
        lista_impar.append(lista_geral[i])

print("Lista geral: ",lista_geral)
print("Números pares: ",lista_par)
print("Números ímpares: ",lista_impar)