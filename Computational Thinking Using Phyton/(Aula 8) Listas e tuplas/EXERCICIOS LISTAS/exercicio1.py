lista_geral = []
lista_par = []
lista_impar = []

for i in range (0,10):
    num = int(input("Digite um número: "))
    lista_geral.append(num)

for i in range (0,10):
    if (lista_geral[i] % 2 == 0):
        lista_par.append(lista_geral[i])
    else:
        lista_impar.append(lista_geral[i])
print(lista_geral)
print(lista_par)
print(lista_impar)
