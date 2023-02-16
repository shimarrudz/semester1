idade = int(input("Digite a idade do competidor: "))

if (idade>= 10 and idade <= 45):

    if (idade >= 10 and idade <= 15):
        print("Categoria Infantil.")
    if (idade >= 16 and idade <= 21):
        print("Categoria Juvenil. ")
    if (idade >= 22 and idade <= 45):
        print("Categoria Adulta")

else:
 print("Idade não permitida!")