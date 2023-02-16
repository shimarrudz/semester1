horas_permanecidas = int(input("Quantas horas você foram permanecidas no estacionamento? "))

valor_a_pagar = 5 * horas_permanecidas

if valor_a_pagar >= 35:
    print("O valor total foi de R$35.00")
else:
    print(f"O valor total foi de R${valor_a_pagar: .2f}")
