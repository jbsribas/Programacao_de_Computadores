#exemplo_3
#Solicita um número ao usuário e mostra os valores de sua
#tabuada.
#import os 
while True:
    print("** Programa Calcula Tabuada **")
    tabuada = 1
    num = int(input("digite um numero inteiro para calcular sua tabuada: "))
    while tabuada <=10 :
        #condição a - mostrar os valores da multiplicação
        print(tabuada, " * ", num, " = ", num*tabuada)
        # condição b - Altere o valor de tabuada, acrescentando mais 1
        tabuada += 1 #tabuada = tabuada +1

    #fora do while tabuada
    ver = input("Deseja sair (s/n): ")
    if ver == 's' or ver == 'S':
        break;
    print(" \n \n")
    
#fora do while True    
print("Terminou !!!")
