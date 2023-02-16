livro = float(input("Digite o preço aqui: "))

if (livro <= 10.00):
    desconto = livro * 0.08
elif (livro <= 60.00):
    desconto = livro * 0.10
else:
    desconto = livro * 0.20
print(f"Preço do livro: R${livro: .2f} - Desconto oferecido: R${desconto: .2f}")
