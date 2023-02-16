n_bloco = int(input("Qual o número do seu bloco? "))

caixa_agua_a = n_bloco % 2


if caixa_agua_a==0:
    print("O bloco é abastecido pela caixa A. ")
else:
    print("O bloco é abastecido pela caixa B. ")
