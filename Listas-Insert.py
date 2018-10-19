# Insert:  Inserção de elemento em uma posição da Lista

a = [1, 2, 12, 23, 45, 67, 'Carlos', 'Eduardo']
a.insert(0, 45)    # Adiciona o elemento 45 na posição 0 da Lista
for x in a:
    print(x, end=' ')

print()
a.insert(7, 55)    # Adiciona o elemento 55 na posição 7 da Lista
for x in a:
    print(x, end=' ')
