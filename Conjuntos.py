# Conjuntos são estruturas de dados que não possuem elementos duplicados.
# Podemos aplicar operações matemáticas aos conjuntos.

a = set('abcdefghijkla')
b = set('abcdefx')
print(type(a))


print(a)          # imprime todas as letras do conjunto a, sem duplicidade

print(a - b)     # imprime o conjunto de letras em a que não estejam não em b

print(a | b)     # imprime o conjunto de letras em a OU em b

print(a & b)     # imprime o conjunto de letras em a E em b

print(a ^ b)     # imprime o conjunto de letras em a OU em b, mas NÃO em AMBOSˆ

########################################################
# Pode-se executar as operações ADD ou POP em conjuntos
#######################################################
a.add('w')       # adiciona o elemento "w" ao conjunto a
print(a)

a.pop()          # Retira o primeiro elemento do conjunto a
print(a)
