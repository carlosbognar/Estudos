# O Objetivo é implementar uma Fila, ou seja, o primeiro elemento inserido é o
#  primeiro a sair (FIFO).

a = [1, 12, 8, 23, -45, 7]

a.append(10)   # Insere o elemento 10 no final da fila
for x in a:
    print(x, end=' ')

print()


a.pop(0)    # Retira o primeiro elemento da Fila --> elemento 1
a.pop(0)    # Retira o segundo elemento da fila  --> elemento 12
for x in a:
    print(x, end=' ')
