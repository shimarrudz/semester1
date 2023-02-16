inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
cont = inicio
quant_pares = 0
quant_impares = 0

while (cont<= fim):
    if (cont % 2 == 0):
        quant_pares = quant_pares + 1
    else:
        quant_impares = quant_impares + 1
    cont = cont + 1

print("Qantidade de pares: ", quant_pares)
print("Quantidade de ímpares: ", quant_impares)

