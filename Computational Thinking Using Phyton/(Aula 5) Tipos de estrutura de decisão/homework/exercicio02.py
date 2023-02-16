ladoa = int(input("Digite o lado do triângulo: "))
ladob = int(input("Digite o outro lado do triângulo: "))
base = int(input("Digite a base do triângulo: "))

if (ladoa==ladob or ladoa==base):
    print("Triângulo isóceles.")

elif (ladoa==ladob==base):
    print("Triângulo equilátero")

elif (ladoa!=ladob!=base):
    print("Triângulo escaleno")

else:
    print("Não corresponde a nenhum tipo de triângulo.")