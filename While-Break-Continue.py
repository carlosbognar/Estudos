# Exemplo de While com cláusulas Break e Continue

while True:
    n = int(input("Digite um valor inteiro:"))
    if n < 0:
        continue  # isso irá voltar a execuçãop ao Loop inicial
    elif n == 0:
        break
    print("O quadrado eh: ", n ** 2)
print("ate mais...")