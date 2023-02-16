string = input("Digite uma frase: ")
string_minuscula = string.lower()
cont_vogais = 0


for letras in (string):
    if letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u":
        cont_vogais += 1

print("A quantidade de vogais: ",cont_vogais)
