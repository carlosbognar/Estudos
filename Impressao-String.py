# Formatando Strings
# Aqui temos um exemplo de utilização de f-strings
name = "Carlos"
language = "Python"
msg = f"{name} loves {language}."
print(msg)


# F-strings fornece uma forma simples e de fácil compreensão para inserir expressões em Python
answer = 42
print(f"The answer is {answer}")

# Outro exemplo de F-Strings e Função datetime.
import datetime
d = datetime.date(2018, 9, 24)
print(f"{d} was a {d:%A}, we started the mailing list back then.")
