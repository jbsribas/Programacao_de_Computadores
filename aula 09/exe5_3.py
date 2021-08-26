#Faça um programa em Pyhton que leia um número digitado
#pelo usuário. Se este for positivo, calcular a sua raiz
#quadrada, senão (se for negativo ou zero) calcular o
#quadrado do valor.

import math

print("Verifica numero")

num = int(input("Digite um numero inteiro: "))

if num >0:
    print("A raiz quadrada de ",num," é: ", math.sqrt(num))
else:
    print("O quadrado de ",num," é: ",num**2)
