'''
Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

# As variáveis estão recebendo números do tipo float
n1 = float(input("Digite o primiero número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número:"))

#Calculo da média e impressão do resultado
media = (n1+n2+n3+n4)/4
print(f"A media entre os número é {media:.2f}")