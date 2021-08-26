#Faça um programa em Pyhton que leia dois números A e B e
#imprima o maior deles.

print("Verifica qual é o maior numero")

a = int(input("Digite o primeiro numero inteiro: "))
b = int(input("Digite o segundo numero inteiro: "))

if a>b:
    print(a," > ",b)

elif a<b:
    print(b," > ",a)
    
else:
    print(a, " = ",b)

#modo 2

if a>b:
    print(a," > ",b)

if a<b:
    print(b," > ",a)
    
if a== b:
    print(a, " = ",b)


#modo 3

if a>b:
    print(a," > ",b)

else:
    if a<b:
        print(b," > ",a)
        
    else:
        print(a, " = ",b)


    

    
