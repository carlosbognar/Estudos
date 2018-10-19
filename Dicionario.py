# Dicionários são conjuntos desordenados de pares chave:valor, onde as chaves são unicas
# Declaramos dicionários utilizando { }
# Utilizamos dicionários para armazenar dados para uma chave particular e retorna-los posteriormente

nome = {'primeiro': 'Carlos', 'segundo': 'Eduardo', 'terceiro': 'Bognar'}
print(nome)
print(type(nome))

print(nome['primeiro'])   # Imprime o elemento cuja chave é 'primeiro'

del nome['primeiro']      # Elimina o elemento cuja chave é 'primeiro'
print(nome)

if 'primeiro' in nome:    # Verifica se a chave 'primeiro' está no dicionário nome
    print("Existe")
else:
    print("Não Existe")

############################################################################
# Pode ser criado um dicionário a partir de Tuplas de pares chave, valor
# Para tanto, use a função dict
############################################################################

salario = dict((('Carlos', '1000,00'), ('Eduardo', '2000,00'), ('Bognar', '3000,00')))

print(salario['Carlos'])

############################################################################
# Pode ser utilizado o méthodo items() para acessar os itens do dicionário
############################################################################

for x, y in salario.items():
    print ("%s  recebe  %s" % (x, y))

############################################################################
# Podemos atribuir um valor default para uma chave que não existe
# Utilizamos dicionario.get(chave, valor_default) para obter um valor default
# quando a chave não existe
############################################################################

print(salario.get('Joao', 0))
#print(salario['Joao'])
#print(salario['Joao'])
