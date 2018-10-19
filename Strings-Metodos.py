#########################################################################
# Método LEN retorna a quantidade de caracteres de um String
########################################################################
s1 = 'Carlos ' 'Eduardo ' 'Bognar'
print(s1)
print(len(s1))   # retorna o tamanho do String

#########################################################################
# Método TITLE retorna a versão TitleCase de um String, ou seja, as palavras
# iniciam com caracteres maiusculos
########################################################################
s2 = 'Carlos eduardo bognar'
print(s2.title())

#########################################################################
# Método UPPER retorna todos os caracteres do String em maiúsculo
########################################################################
s3 = 'Carlos eduardo bognar'
print(s3.upper())

#########################################################################
# Método LOWER retorna todos os caracteres do String em maiúsculo
########################################################################
s4 = 'CARLOS Eduardo Bognar'
print(s4.lower())

#########################################################################
# Método ISALPHA verifica se todos os caracteres no String são alfabeticos
# Importante: o espaço em branco não é considerado Alfabetico
########################################################################
s5 = 'CARLOS1'
print(s5.isalpha())

#########################################################################
# Método ISDIGIT verifica se todos os caracteres no String são numéricos
# Importante: o espaço em branco não é considerado numérico
########################################################################
s6 = '123456'
print(s6.isdigit())

#########################################################################
# Método ISLOWER verifica se todos os caracteres no String são minúsculos
########################################################################
s7 = 'Carlos'
print(s7.islower())

