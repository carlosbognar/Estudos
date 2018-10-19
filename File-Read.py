###########################################################################################
# Para ler um arquivo é necessário abri-lo antes.
# Seguem algune exemplos de leitura de arquivos
#
# Após sua utilização, o arquivo deve ser fechado com a função CLOSE
############################################################################################

Path = "/Volumes/HDD/Users/carlos/Desktop/Arquivos/arquivo.txt"
fobj = open(Path)
texto = fobj.read()
print("=" * 50, "Primeira Leitura")
print(texto)

print("=" * 50, "Segunda Leitura")
texto2 = fobj.read()                 # Como EOF foi encontrado, nenhum novo registro do
print(texto2)                        # arquivo foi lido. A função read() retorna um
fobj.close()                         # String vazio.

###########################################################################################
# Para ler um registro por vez (linha) do arquivo pode-se utilizar o método
# READLINE().
############################################################################################

fobj = open(Path)
texto = fobj.readline()               # Lê apenas uma linha do arquivo
print("=" * 50, "Terceira Leitura")
print(texto)
fobj.close()

###########################################################################################
# Para ler todas as linhas do arquivo em uma Lista pode-se utilizar o método
# READLINES().
############################################################################################

fobj = open(Path)
lista = fobj.readlines()               # Lê todas as linhas do arquivo em uma Lista
print("=" * 50, "Quarta Leitura")
print(lista)
fobj.close()

###########################################################################################
# Pode-se ler todas as linhas do arquivo em um Loop
#
############################################################################################
print("=" * 50, "Quinta Leitura")
fobj = open(Path)
for x in fobj:
    print(x, end=' ')

fobj.close()

###########################################################################################
# Leitura do arquivo em um CENÁRIO REAL
# Utiliza a cláusula WITH, que cuida do fechamento automático do arquivo
############################################################################################
print("=" * 50, "Sexta Leitura")

with open(Path) as fobj:
    for line in fobj:
        print(line)

