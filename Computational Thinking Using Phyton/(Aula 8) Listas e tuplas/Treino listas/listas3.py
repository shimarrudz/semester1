listas_medias = []
mediasmaior7 = []

for i in range(0,5):
    n1 = float(input("Digite uma nota: "))
    n2 = float(input("Digite uma nota: "))
    n3 = float(input("Digite uma nota: "))
    media = (n1 + n2 + n3) / 3
    listas_medias.append(media)

for i in range(0,10):
    if (listas_medias > 7):
        mediasmaior7 += mediasmaior7 + 1
print(listas_medias)
print("A quantidade de média maiores que 7: ", mediasmaior7)