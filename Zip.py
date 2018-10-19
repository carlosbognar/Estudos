# ZIP: Permite iteragir com elementos de duas sequencias simultaneamente
# dentro de um mesmo Loop

a = ['Carlos', 'Eduardo', 'Bognar']
b = ['1000,00', '2000,00', '3000,00']

for i, j in zip(a, b):
    print("%s  recebe  %s" % (i, j))