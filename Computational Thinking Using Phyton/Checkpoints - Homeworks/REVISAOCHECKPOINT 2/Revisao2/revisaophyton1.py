resposta = 1
total_geral = 0

print("01 - XXXXX -R$ 35,00")

while(resposta != 0):
    quantidade = int(input("Digite a quantidade do item: "))
    codigo = int(input("Digite o código do item: "))

    if(codigo == 01):
        total_geral = total_geral + (quantidade * 35.00)
    elif(codigo == 02):
        .


    resposta = int("Deseja continuar (1-SIM / 0-NÃO): ")

print(f"O valor total é de: {total_geral:.2f}")