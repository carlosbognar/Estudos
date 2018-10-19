# Extend: Adiciona elementos na Lista. No caso, serão adicionados os elementos
# da Lista b na Lista a

a = [1, 2, 12, 23, 45, 67, 'Carlos', 'Eduardo']
b = ['x', 'y', 'z']
a.extend(b)    # Adiciona os valores da lista b na lista a, não a lista b propriamente dita
for x in a:
    print(x, end=' ')

print()
print(a[-1])