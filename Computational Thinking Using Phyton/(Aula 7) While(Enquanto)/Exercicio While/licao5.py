senha_valida = 50
tentativa_senha = int(input("Digite uma senha com dígitos (0-99): "))

while (tentativa_senha != senha_valida):
    tentativa_senha = int(input("Senha incoreta,digite-a novamente entre (0-99): "))

print("Senha correta! ")
