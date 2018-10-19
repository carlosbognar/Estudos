# Tuplas são dados separados por vírgula
# Tuplas são imutáveis, ou seja, não se pode utilizar DEL/ADD/EDIT em valores da tupla

a = 'Carlos', 'Eduardo', 'Bognar'
for x in a:
    print(x, end=' ')

print()
print(a[1])  # Imprime o segundo elemento da Tupla, como se fosse uma Lista.