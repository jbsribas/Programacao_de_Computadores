# exemplo 1 estrutura aninhada

#verificar qual valor é maior que o outro
#maneira de fazer 1

num1 = int(input("digite o primeiro numero: "))

num2 = int(input("digite o segundo numero: "))

if(num1 < num2):
    print("o primeiro numero é menor que o segundo numero")

else:
    if(num1==num2):
        print("Os numeros são iguais")
    else:
        print("o segundo numero é menor que o primeiro numero")

#####################################################        
# teste 2
print("**************************************")
if(num1 <= num2):
    if(num1==num2):
        print("Os numeros são iguais")
    else:
        print("o primeiro numero é menor que o segundo numero")
else:
        print("o segundo numero é menor que o primeiro numero")


#############################################################
#exemplo 2, verificar se os numeros digitados são maiores que 2
print("******************************************")
if num1 > 2 :
       if num2 > 2:
           print("Os dois numeros são maiores que 2")
else:
    print("um dos dois numeros não é maior que 2")


print("***************************************")
if num1 >2  and num2 >2:
    print("Os dois numeros são maiores que 2")

else:
    print("um dos numeros não é maior que 2")







          



