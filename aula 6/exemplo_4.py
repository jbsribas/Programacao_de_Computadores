#Um triângulo será equilátero se seus três ângulos são iguais.
#Um triângulo com dois de seus ângulos iguais é chamado de isósceles .
#Um triângulo com três ângulos diferentes é chamado de escaleno
#A soma dos três ângulos de um triângulo deverá ser 180º,
#senão não é um triângulo.

angulo1 = float(input("digite o primeiro angulo: "))

angulo2 = float(input("digite o segundo angulo: "))

angulo3 = float(input("digite o terceiro angulo: "))

soma = angulo1+angulo2+angulo3

if (soma == 180):
    if angulo1 == angulo2 and angulo2 == angulo3 :
        print(" O triangulo é equilátero")
        
    elif angulo1 == angulo2 or angulo1== angulo3 or angulo2 == angulo3:
        print("O triangulo é isósceles") 

    else:
        print("o triangulo é escaleno ")
else:
    print("Não é um triangulo, pois a soma dos angulos não é 180°")


    
