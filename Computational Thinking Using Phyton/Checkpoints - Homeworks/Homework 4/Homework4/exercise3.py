mercadoria = float(input("Qual o valor da mercadoria que você deseja comprar? "))
saldo = float(input("Qual o saldo da sua conta? "))
falta = mercadoria - saldo

if saldo >= mercadoria:
    print("Transição aprovada!")
else:
    print(f"Saldo insuficiente. Para efetuar a compra faltaram {falta: .2f}")