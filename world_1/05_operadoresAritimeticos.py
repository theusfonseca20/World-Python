# Operadores Aritméticos
# +, -, *, /, //, **, %
# Ordem de precedência: (), **, *, /, //, %, +, -

#Exemplos de operações aritméticas:
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 * num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2
resto = num1 % num2
exponenciacao = num1 ** num2

print(f"A soma é {soma}")
print(f"A subtração é {subtracao}")
print(f"A multiplicação é {multiplicacao}")
print(f"A divisão é {divisao:.2f}")
print(f"Resto da divisão é {resto}")
print(f"exponenciação é {exponenciacao}")

# Operação de comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2
# Se eu imprimir essas variáveis, o resultado será True ou False
# Exemplo:
print(f"O primeiro número é maior que o segundo? {bigger}")
