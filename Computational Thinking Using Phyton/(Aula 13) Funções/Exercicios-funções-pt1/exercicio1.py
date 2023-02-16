'''Uma função com dois parâmetros (a e b) que verifique e retorne o maior deles;'''
##Começando funcao

    #Nome da função
def verifica_maior(a,b):
    if (a > b):
        return a
    else:
        return b


#inputando os valores de A e B
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

                            #Chamando a função / aqui ele executa return o valor
print("O maior número é: ", verifica_maior(a,b))

