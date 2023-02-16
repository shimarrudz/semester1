lista_palavras = []
qtde_palindromas = 0

for i in range (0,10):
    lista_palavras.append(input("Digite a palavra: "))

for i in range (0,10):
    if (lista_palavras[i] == lista_palavras[i][::-1]):
        qtde_palindromas+=1

print("Quantidade de palindromos: ", qtde_palindromas)
