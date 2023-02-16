'''Uma função que calcule e retorne o somatório e a média dos elementos da lista.'''

def carrega_lista(lista):
    for i in range(0,10):
        lista.append(int(input("Digite o elemento: ")))
    return lista


def operacoes_lista(lista):
    soma = 0
    tam = len(lista)
    for i in range(0,tam):
        soma += lista[i]
    media = soma / tam
    return soma, media

lista = []

carrega_lista(lista)

soma, media = operacoes_lista(lista)

