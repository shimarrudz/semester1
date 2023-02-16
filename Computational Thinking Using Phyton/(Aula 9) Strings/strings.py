nome = "Shima"
print(type(nome))
print(nome[0])
print(nome[3])
print(nome[0:3])
print(nome[-3:])
print(len(nome))
sobrenome = "Serete"
nomecompleto = nome + " " + sobrenome
print(nomecompleto)
if nome == sobrenome:
    print("Strings iguais")
else:
    print("Strings diferentes")


frase = "Programar em Phyton é legal"
print(frase.find("legal"))
print(frase.find("Phyton"))

nova_frase = frase.replace("legal", "top")
print(nova_frase)

nova_frase = frase.split(" ")
print(nova_frase)
print(nova_frase[2])

texto = "Programar_em_Phyton"
texto_split = texto.split("_")
print(texto_split)

texto_minuscula = texto.lower()
print(texto_minuscula)

texto_maiuscula = texto.upper()
print(texto_maiuscula)

textodois = "Pipo"
texto_invertido = textodois[::-1]
print(texto_invertido)




