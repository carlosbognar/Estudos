# APPEND-Lista: Adiciona uma  uma Lista em outra Lista.
# Note que a Lista adicionada é tratada como um único elemento

a = [1, 2, 12, 23, 45, 67, 'Carlos', 'Eduardo']
b = ['x', 'y', 'z']
a.append(b)    # Adiciona a lista b na lista a. A lista b é tratada como um único elemento
for x in a:
    print(x, end=' ')

print()
print(a[-1])