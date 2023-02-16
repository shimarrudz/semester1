canetas = float(input("Quantas canetas voce irá adquirir? "))
canetaspreço = float(input("Qual o preço dela? "))
caderno = float(input("Quantos cadernos você irá adquirir? "))
cadernospreço = float(input("Qual o preço do caderno? "))
lapis = float(input("Quantos lápis você irá adquirir? "))
lapispreço = float(input("Qual o preço do lápis? "))


valor_canetas = (canetas * canetaspreço)
descontocaneta = (valor_canetas) - valor_canetas * 0.05

valor_caderno = (caderno * cadernospreço)
descontocaderno = (valor_caderno) - valor_caderno * 0.20

valor_lapis = (lapis * lapispreço)

valor_total = descontocaderno + descontocaneta + valor_lapis

print(f"O valor total das canetas é de {valor_canetas: .2f} - Desconto oferecido R${descontocaneta: .2f} ")
print(f"O valor total dos cadernos é de {valor_caderno: .2f} - Desconto oferecido R${descontocaderno: .2f} ")
print(f"O valor total dos cadernos é de {valor_lapis: .2f}")
print("O valor total foi de :", valor_total)

