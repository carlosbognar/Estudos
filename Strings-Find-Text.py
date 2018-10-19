#########################################################################
# O método FIND permite encontrar um texto / substring em um string
# FIND retorna a posição em que o texto foi encontrado
# Se o valor não for encontrado, retorna -1
########################################################################
s1 = 'Eu gosto de programar em Python'

print(s1.find("E"))      # irá retornar o valor 0 --> primeira posição
print(s1.find("gosto"))  # irá retornar o valor 3
print(s1.find("x"))      # x não existe no string, logo retorna -1