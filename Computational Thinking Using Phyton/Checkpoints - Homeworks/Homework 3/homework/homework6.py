eleitores = input("Qual o número total de eleitores do seu município?")
eleitores = int(eleitores)
voto_branco = input("Quantidade de votos em branco?")
voto_branco = int(voto_branco)
voto_nulo = input("Quantidade de votos nulos?")
voto_nulo = int(voto_nulo)
voto_valido = input("Quantidade de votos válidos?")
voto_valido = int(voto_valido)



percentual_votos_brancos = (voto_branco/eleitores)*100
print("% Votos Brancos :", percentual_votos_brancos)
percentual_votos_nulos = (voto_nulo/eleitores)*100
print("% Votos Nulos :", percentual_votos_nulos)
percentual_votos_validos = (voto_valido/eleitores)*100
print("% Votos Válidos:", percentual_votos_validos)


