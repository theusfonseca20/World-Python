import math
import statistics

#1 - Acessar o numero pi
print(math.pi)
print(f"{math.pi:.2f}")

#2 - Acessar o numero de euler
print(math.e)
print(f"{math.e:.2f}")

#3 - Arredondamento 
num1 = 10.4
print(math.ceil(num1))
print(math.floor(num1))

#4 - Fatorial de numero
num2 = 7
print(math.factorial(num2))

#5 - Potencia de numeros
print(math.pow(5,5))

#6 - Raiz quadrara
print(math.sqrt(169))

#7 - media
print(statistics.mean([1,2,3,4,5,6,7,8,9,10]))

#8 - Mediana
print(statistics.median([1,2,3,8,9,10]))

#9 - Moda
print(statistics.mode([2,5,6,3,2,9,4,2,5,6,2,2,4,7,2]))

#10 - Desvio Padrão
print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5]))