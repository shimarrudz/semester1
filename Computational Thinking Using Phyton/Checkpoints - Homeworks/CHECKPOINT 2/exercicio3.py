resp = 1
soma_valor = 0
quant_mercadorias = 0

while (resp != 0):
    quant = int(input("Digite a quantidade em estoque: "))
    valor = float(input("Digite o valor da mercadoria: "))
    soma_valor = soma_valor + (quant * valor)
    quant_mercadorias += quant  #quant_mercadorias = quant_mercadorias + quant
    resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

media_valor = soma_valor / quant_mercadorias

print(f"Valor total das mercadorias: {soma_valor:.2f}")
print(f"Média do valor das mercadorias: {media_valor:.2f}")
