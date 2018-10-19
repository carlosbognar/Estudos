###########################################################################################
# Exemplo de Passagem de Argumentos para Programas a partir da Linha de Comando
# Utilizamos a biblioteca SYS
# IMPORTANTE:  Na linha de Comando digitar:
#
# python3  nome_do_programa   Lista_de_Argumentos
#
# Exemplo: python3  /Volumes/HDD/Users/carlos/PycharmProjects/Nome_do_Projeto/Nome_do_Programa.py argum1 argum2
############################################################################################

import sys
print("Primeiro argumento", sys.argv[0])
print("Demais argumentos")

for i, x in enumerate(sys.argv):
    print(i, x)