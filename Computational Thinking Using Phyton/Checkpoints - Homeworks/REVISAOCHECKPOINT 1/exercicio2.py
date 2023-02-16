macas_compradas = float(input("Quantas maças você deseja comprar? "))

if macas_compradas <= 12:
    umaduzia = macas_compradas * 1.30

    print(f"Sua compra custou: {umaduzia: .2f}")



if macas_compradas >= 12:
    umaduzia = macas_compradas * 1.00

    print(f"Sua compra custou: {umaduzia: .2f}" )
