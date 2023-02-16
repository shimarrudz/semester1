ano = int(input("Digite um ano entre 1000 e 2999: "))


if (ano>= 1000 and ano <= 2999):

   if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Ano bissexto")
   else:
    print("Não é bissexto")


else:
    print("Ano inválido!")







