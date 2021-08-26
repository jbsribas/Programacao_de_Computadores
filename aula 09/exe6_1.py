#Altere a calculadora com as quatro operações básicas
#matemáticas. Informe ao usuário caso ele realize uma
#divisão por zero. Utilize uma estrutura aninhada e visualize
#“Operador errado” caso aconteça.

print(" ** Calculadora ** ")
print("[] + \n[] - \n[] * \n[] /")

op = input("Digite o sinal de operação ")

if op == '+' or op == '-' or op == '*' or op=='/':
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    calc = 0
    if op== '+':
        calc = num1 + num2
        
    elif op=='-':
        calc = num1 - num2

    elif op == '*':
        calc = num1 * num2

    else:
        if num2 == 0:
            print(" Não existe divisão por zero!!!",
                  "\n Por favor entre com um valor válido")
        else:
             calc = num1 / num2
    print(calc)
else:
    print("Operador invalido!!")
