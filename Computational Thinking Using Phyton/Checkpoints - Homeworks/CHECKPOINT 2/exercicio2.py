qtde_negativos = 0

for i in range(1,11):
    num = int(input("Digite um número: "))
    if (num < 0):
        qtde_negativos = qtde_negativos + 1

print("Quantidade de número negativos: ", qtde_negativos)
