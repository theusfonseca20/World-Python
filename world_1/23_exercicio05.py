"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

salario = float(input("Digite o seu salário: "))
if salario > 1250: #Maior que 1250 execute o codigo no bloco if:
    novoSalario = salario + (salario*0.10)
else: #SE NAO, execute o codigo no bloco else:
    novoSalario = salario + (salario*0.15)
print(f"Seu novo salário é de {novoSalario:.2f} reais")