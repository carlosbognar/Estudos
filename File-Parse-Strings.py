###########################################################################################
# O programa a seguir é um exemplo de PARSER em um arquivo TXT
# No caso do programa, vamos contar quantos espaços em branco, TAB e Linhas tem o arquivo
#
# IMPORTANTE: Utilizamos o método PATCH.EXISTS para validar o path do arquivo
#
############################################################################################

import sys
import os

# O Método PARSE_FILE faz o PARSER e conta os espaços, TBS e linhas do arquivo
def parse_file(path):
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i, line in enumerate(fd):
        spaces += line.count(' ')   # contabiliza o espaço
        tabs += line.count(' \t')   # contabiliza o TAB
    fd.close()
    return spaces, tabs, i + 1      # retorna as quantidades de espaços, TABs e Linhas

# O Método principal chama a função de PARSER e imprime os resultados
def main(path):
    if os.path.exists(path):        # verifica se o caminho e nome do arquivo existem
        spaces, tabs, lines = parse_file(path)
        print("Espacos  %d. tabs %d. linhas %d" % (spaces, tabs, lines))
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)