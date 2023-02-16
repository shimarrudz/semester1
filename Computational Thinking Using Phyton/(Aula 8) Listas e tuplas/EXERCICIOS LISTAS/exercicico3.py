lista_medias = []
quant_mediasmaiores7 = 0

for i in range(0,5):
    n1 = float(input("Digite uma nota: "))
    n2 = float(input("Digite uma nota: "))
    n3 = float(input("Digite uma nota: "))
    media = (n1 + n2 + n3) / 3
    lista_medias.append(media)

for i in range (0,10):
    if (lista_medias[i] >= 7.0):
        quant_mediasmaiores7 = quant_mediasmaiores7 + 1

print(lista_medias)
print("Quantidade de alunos com média maior que 7.0: ", quant_mediasmaiores7)

