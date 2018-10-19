###########################################################################################
# Para GRAVAR um arquivo pode-se utilizar o método
# WRITE().
############################################################################################
Path = "/Volumes/HDD/Users/carlos/Desktop/Arquivos/arquivo2.txt"

fobj = open(Path, 'w')
fobj.write('teste de gravacao de arquivo\n')    # Grava uma linha no arquivo
fobj.write('Carlos\n')
fobj.write('Eduardo\n')
fobj.write('Bognar')

fobj.close()