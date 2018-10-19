#########################################################################
# Método SPLIT retorna uma lista de partes do string, conforme o argumento
# que será utilizado para Split
########################################################################
s8 = 'Carlos Eduardo Bognar'
lista = s8.split(" ")
print(lista)

s9 = 'Carlos: 1000:Eduardo:2000:Bognar:3000'
lista2 = s9.split(":")
print(lista2)

#########################################################################
# Método JOIN é oposto ao Split, ou seja, ele pega uma lista contendo
# strigs e a junta
########################################################################
s10 = "-".join("Carlos Eduardo Bognar".split(" "))
print(s10)
