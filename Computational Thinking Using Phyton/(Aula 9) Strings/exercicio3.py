palavra = input("Digite a string: ")

palavra_invertida = palavra[::-1]

if(palavra == palavra_invertida):
    print("Palíndromo")
else:
    print("Não é Palíndromo")
