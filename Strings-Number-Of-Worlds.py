#########################################################################
# O método LEN combinado com o método SPLIT permite a contagem do número
# de palavras em uma determinada linha
########################################################################
s = input("Entre com uma linha de texto: ")

print("O numero de palavras na linha é %d " % (len(s.split(" "))))