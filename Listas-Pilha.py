# O Objetivo é utilizar uma Lista como Pilha (STACK)
# POP-Lista: Retira um elemento da Pilha (POP)

a = [1, 12, 8, 23, -45, 7, 6, 10, 'Carlos', 'Eduardo']
a.pop()    # Retira o elemento 'Eduardo' da Lista - Último
a.pop()    # Retira o elemento 'Carlos da Lista - Último
a.pop()    # Retira o elemento 10 da Lista - Último
for x in a:
    print(x, end=' ')

print()
a.append(34)   # Insere o elemento 34 no final da Lista
for x in a:
    print(x, end=' ')

# Exemplo de retirada de um elemento de uma posição especifica da Lista

print()
a.pop(2)   # Retira o segundo elemento da Lista
for x in a:
    print(x, end=' ')