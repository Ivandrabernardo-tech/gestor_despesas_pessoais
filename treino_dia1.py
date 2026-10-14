iva = 0.21
taxa_dolar = 1.10

nome = input("Escreva o teu nome: ")
print("Bom dia " + nome + "!")


preco = float(input("Escreva o valor: "))
iva_acrescimo = preco*iva + preco
print("São: " + str(iva_acrescimo) + "£")


quantia = float(input("Qual é a quantia ? "))
dolares = quantia * taxa_dolar

print(f"Em dólares esta quantia   {quantia:.2f}  esta a {dolares:.2f}  dólares")