# REMOVE-Lista: Remove uma Lista de outra Lista.
# Note que a Lista removida é tratada como um único elemento

a = [1, 2, 12, 23, 45, 67, 'Carlos', 'Eduardo']
b = ['x', 'y', 'z']
a.append(b)    # Adiciona a lista b na lista a. A lista b é tratada como um único elemento
for x in a:
    print(x, end=' ')

print()


a.remove(b)     # Remove a lista b da lista a
for x in a:
    print(x, end=' ')