#Faça um programa em Pyhton que leia um número N e
#imprima “F1”, “F2” ou “F3”, conforme a condição:
#➢ “F1”, se N <= 10
#➢ “F2”, se N > 10 e N <= 100
#➢ “F3”, se n > 100

n = int(input("Digite um numero inteiro: "))

#primeira forma
if n <=10:
    print("F1")

if n> 10 and n<=100:
    print("F2")

if n>100:
    print("F3")

#segunda forma

if n<=10:
    print("F1")
    
else:
    if n>10 and n<=100:
        print("F2")
    else:
        print("F3")

# terceira forma

if n <=10:
    print("F1")
    
elif n>10 and n<=100:
    print("F2")

else:
    print("F3")











        
   
