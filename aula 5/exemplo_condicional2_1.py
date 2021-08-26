#Exemplo_condiconal 2

#Faça um programa Python que leia um número qualquer
#e o verifica se é par ou ímpar Se for par,
#imprimir uma mensagem “O número é par”
#Caso contrário, imprimir o número é ímpar”

import os  


numero = float(input("digite o numero:" ))

resto = numero%2

if resto==1:
    print("ímpar")
else:
    print("par")
    
#outra maneira de fazer é colcoar o calculo da divisão pegando
#o resto ja dentro do if entre parenteses
    
print("*********** ")
if (numero%2)==0:
    print("par")
else:
    print("ímpar")
print("\n")
os.system("pause")
