portugues = []
ingles = []
resp = 1

while (resp!=0):
    ingles.append(input("Palavra em ingles: "))
    portugues.append(input("Palavra em portugues: "))
    resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

palavra_ingles = input("Digite a palavra em inglês a ser traduzida: ")

if (palavra_ingles in ingles):
    indice_palavra = ingles.index(palavra_ingles)
    print("Tradução: ", portugues[indice_palavra])


