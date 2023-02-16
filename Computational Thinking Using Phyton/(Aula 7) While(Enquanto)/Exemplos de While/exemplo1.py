numero = int(input("Digite o número da tabuada que voce deseja calcular: "))

i = 0

while(i <= 10): ##Enquanto "i" for menor ou igual a zero.
    tabuada = numero * i
    print(numero, " X ", i, "=", tabuada)
    i = i + 1
