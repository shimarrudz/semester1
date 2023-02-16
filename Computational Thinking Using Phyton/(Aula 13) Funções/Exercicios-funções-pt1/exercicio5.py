'''Uma função que faça a leitura de uma lista com 10 números inteiros como parâmetro e que retorne essa
lista devidamente preenchida;'''

def carrega_lista(lista):
    for i in range(0,10):
        lista.append(int(input("Digite o elemento: ")))
    return lista


#Declarando lista
lista = []

print("Lista carrega ",carrega_lista(lista))

