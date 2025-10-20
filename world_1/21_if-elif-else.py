num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a opção desejada(+, -, *, /)")

if operation == "+":
    result = num1+num2
    print(f"O resultado da soma entre {num1} e {num2} é: {result}")
elif operation == "-":
    result = num1-num2
    print(f"O resultado da subtração entre {num1} e {num2} é: {result}")
elif operation == "*":
    result = num1*num2
    print(f"O resultado da multiplicação entre {num1} e {num2} é: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1/num2
        print(f"O resultado da divisão entre {num1} e {num2} é: {result:.2f}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")