inicio = int(input("Digite o ínicio: "))
fim = int(input("Digite o fim: "))

contador = inicio + 1

while(contador <= fim - 1):
#(contador < fim) também está certo
    print(contador)
    contador = contador + 1
