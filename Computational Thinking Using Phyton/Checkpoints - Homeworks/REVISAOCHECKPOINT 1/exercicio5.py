fritas = float(input("Quantas fritas foram consumidas? "))
pasteis= float(input("Quantos pasteis foram consumidos? "))
cerveja = float(input("Quantas cervejas foram consumidas? "))
quantamigos = int(input("Vocês estão em quantas pessoas? "))
total_fritas = fritas * 35.00
total_pasteis = pasteis * 25.00
total_cerveja = cerveja * 18.00
total_conta = (total_cerveja + total_fritas + total_pasteis)
valor_p_cadapessoa = total_conta / quantamigos

print(f"O valor total da conta foi de: {total_conta: .2f} ")
print(f"O valor indivudual é de: {valor_p_cadapessoa: .2f}")
