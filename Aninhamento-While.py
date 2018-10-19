# Esse programa faz aninhamento de While. Note que a tabulação define o encerramento de um bloco.
# A clausula print("-" * 50) irá imprimir o traço 50 vezes.
# A cláusula print() quebra a linha

i = 1
print("-" * 50)
while i < 11:
    n = 1
    while n <=10:
        print ("%4d" % (i * n), end=' ')
        n = n + 1
    print()
    i = i + 1
print("-" * 50)
