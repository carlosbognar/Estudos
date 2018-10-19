###########################################################################################
# Arquivos podem ser de texto ou binários. Antes de utilizá-los é necessário
# abri-los com a função OPEN. A função OPEN requer dois parâmetros:
# o nome do arquivo (ou caminho) e o modo de abrtura, que pode ser:
#
# "r" --> apenas leitura, não pode ser editado ou deletado.
# "w" --> gravação, se o arquivo exitir serão deletados todos os registros e será aberto para gravação
# "a" --> será aberto em modo append.
#
# Após sua utilização, o arquivo deve ser fechado com a função CLOSE
############################################################################################

Path = "/Volumes/HDD/Users/carlos/Desktop/Arquivos/arquivo.txt"
fobj = open(Path)
texto = fobj.read()
print(texto)
fobj.close()