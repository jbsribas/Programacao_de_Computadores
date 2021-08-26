#Crie um programa que calcule/visualize o Índice de Massa
#Corpórea (IMC) e visualize uma mensagem conforme a
#tabela abaixo:

print("** Calculo IMC **")

peso = float(input("Digite o peso (Kg): "))
altura =  float(input("Digite a altura (m): "))
genero = input("Digite M para mulher ou H para homem: ")

imc= peso/altura**2

if genero == 'M' or genero == 'm':
    if imc < 19.1:
        print("Abaixo do peso ideal")
        
    elif imc >= 19.1 and imc < 25.8:
        print("No peso ideal")
        
    elif imc >= 25.8 and imc < 27.3:
        print("Marginalmente acima do peso")
        
    elif imc >= 27.3 and imc < 32.3:
        print("Acima do peso ideal ")

    else:
        print("Obesa")
        
elif genero == 'H' or genero == 'h':
     if imc < 20.7:
        print("Abaixo do peso ideal")

     elif imc >= 20.7 and imc < 26.4:
        print("No peso ideal")
     elif imc >= 26.4 and imc < 27.8:
        print("Marginalmente acima do peso")
        
     elif imc >= 27.8 and imc < 31.1:
        print("Acima do peso ideal ")

     else:
        print("Obeso")
else:
    print("Digite o genero corretamente!!")





    
    
