'''Uma função com um parâmetro n que verifique se ele é par ou ímpar. Caso ele seja par, retorne 1;
 caso contrário, retorne 0;'''


def verifica_parimpar(n):
    if (n % 2 == 0):
        return 1
    else:
        return 0

n = int(input("Digite o valor de n: "))
print("Resultado da função: ", verifica_parimpar(n))
if(verifica_parimpar(n)==1):
    print("par")
else:
    print("ímpar")
