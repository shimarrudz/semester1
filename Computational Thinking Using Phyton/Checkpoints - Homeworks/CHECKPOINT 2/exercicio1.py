total_geral = 0

preco = float(input("Digite o valor do produto: "))

while (preco!= 0.00):
    quant = int(input("Digite a quantidade do produto: "))
    total_geral += quant * preco
    preco = float(input("Digite o valor do produto: "))

print(f"Valor total a pagar: {total_geral:.2f}")
