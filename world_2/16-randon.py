import random

#1 - Selecionar valor aleatorio de uma lista
List1 = [7,6,4,3,2,1]
print(random.choice(List1))

#2 - Gera um numero aleatorio em um intervalo de valores
r1 = random.randint(5,15)
print(r1)

#3 - Seleciona caractere obrigatorio de uma string
name = "Curso de python"
r2 = random.choice(name)
print(r2)