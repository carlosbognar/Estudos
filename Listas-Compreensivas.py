# Listas compreensivas são uma forma de criar listas a partir de expressões.
# As expressões podem ser formadas for FOR

a = [1, 2, 3]

b = [x ** 2 for x in a]  # Essa expressão irá elevar ao quadrado cada elemento da lista a
for x in b:
    print(x, end=' ')

print()

c = [x + 1 for x in [x ** 2 for x in a]]  # Essa expressão irá somar 1 a cada elemento elevado ao quadrado
for x in c:                               # a partir da lista a
    print(x, end=' ')

print()
