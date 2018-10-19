#########################################################################
# EXEMPLOS 1 e 2: Vamos definir um valor default para um argumento de
# função, caso ele seja chamada sem passarmos o valor.
########################################################################
print("=" * 50, "Exemplo 1")

def compara(a, b=-99):
    if a > b:
        return True
    else:
        return False

print(compara(1, 2))
print("=" * 50, "Exemplo 2")

print(compara(5))  # A função está sendo chama sem receber argumento de b
                   # portanto, o valor -99 é atribuído a variável b

#########################################################################
# EXEMPLOS 3, 4 e 5: Passagem de valores e valores defaul.
# Vamos utilizar como argumento da chamada a atribuição de valores
########################################################################
print("=" * 50, "Exemplo 3")

def func(a, b=5, c=10):
    print ("a = ", a, " e b = ", b , " e c = ", c)

func(12, 24)  # O argumento c não foi passado, assumiu o default

print("=" * 50, "Exemplo 4")
func(12, c=24)  # O argumento 24 foi atribuído a variavel c. B assume o default.


print("=" * 50, "Exemplo 5")
func(b=12, c=24, a=-1)  # Os três argumentos foram atribuídos, porém foram de ordem.