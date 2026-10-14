print("=== Gestor de Despesas Pessoais ===")
descricao = input("De que despesa trata-se: ")

valor = float(input("Qual é o valor da despesa? "))

if valor <= 0:
    print("Erro: O valor tem de ser maior que zero")
else:

    print(f"Despesa registada: {descricao}, {valor:.2f}€")


