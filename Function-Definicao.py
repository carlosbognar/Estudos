#########################################################################
# Utilizamos DEF para definir uma função.
# Podemos passar e receber valores de funções
########################################################################

def soma(a, b):
    return(a + b)

print(soma(12.5, 10)) # Chama a função passando parâmetros


#########################################################################
# Exemplo de Variáveis de Escopo Local e Global
########################################################################

def altera():
    a = 90
    print(a)

a = 9
print("Antes de chamar a funcao: ", a)
print("Dentro da Funcao: ", end=' ')
altera()
print("Depois de chamar a funcao: ", a)


#########################################################################
# Podemos definir uma variavel Global dentro da função, utilizando
# o atributo GLOBAL
########################################################################
print("*" * 50)
def altera():
    global a   # Torna o escopo de a global
    a = 90
    print(a)

a = 9
print("Antes de chamar a funcao: ", a)
print("Dentro da Funcao: ", end=' ')
altera()
print("Depois de chamar a funcao: ", a)