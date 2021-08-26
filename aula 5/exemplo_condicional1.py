#exemplo1 condicional

#Faça um programa Python que leia um número qualquer e
#o imprima,caso este seja positivo

numero = float(input("Digite um numero qualquer: "))
if numero>0:
    print("o numero ",round(numero), " é positivo")
elif numero ==0: 
    print("o numero é zero e consideramos neutro")
else:
    print("o numero digitado é negativo")

  
## elif seria :: else:
                   #if numero == 0:

