# Uso de Operadores: Soma
a = 2
b = 3
print(a + b)

# Uso de Operadores: Subtração
a = 2
b = 3
print(a - b)

# Uso de Operadores: Módulo
a = 14
b = 3
print(14 % 3)

# Uso de Operadores Relacionais
a = 1
b = 2
print(a < b)
print(a > b)
print(a != b)
print(a == b)

# Uso de Expressões
a = 9
b = 12
c = 3
x = a - b / 3 + c * 2 - 1
y = a - b / (3 + c) * (2 - 1)
z = a - (b / (3 + c) * 2) - 1
print("X = ", x)
print("Y = ", y)
print("Z = ", z)

# Conversão de Tipos
sum = 0.0
for i in range(1, 11):
    sum = sum + 1 / i
    print("%2d %6.4f" % (i, sum))