# Leitura de Dados Decimais pelo teclado

quantidade = float(input("Entre com a quantidade: "))
taxa = float(input("Entre com a taxa: "))
periodo = int(input("Entre com o periodo: "))
value = 0
year = 1
while year <= periodo:
    value = quantidade + (taxa * quantidade)
    print("Ano %d Rs. %.2f" % (year, value))
    quantidade = value
    year = year + 1

