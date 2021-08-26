# quadrado da soma dos valores lidos

print("** quadrado da soma ** ")

a = int(input("Digite um número inteiro: "))

b = int(input("Digite outro número inteiro: "))

calc1 = (a+b)**2
calc2 = a**2 + (2*(a*b))+b**2
calc3 = a*a +2*a*b +b*b

print(" O quadrado da soma dos numeros é: ", calc1,
       "\n ou ", calc2, "\n ou", calc3)
