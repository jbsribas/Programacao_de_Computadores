# exemplo_5

#Apresente um menu de opções para o cálculo das seguintes
#operações entre dois números digitados pelo usuário

while True:
    print("** Programa calculadora **")
    print("Digite uma das opções abaixo:")
    print("\t + = Soma")
    print("\t - = Subtração")
    print("\t * = Multiplicação")
    print("\t / = Divisão")
    print("\t qualquer outra tecla =Sair")
    ver = input("Digite a opção desejada: ")
    if(ver =='+'):
       n1 = float(input("digite um numero: "))
       n2 = float(input("digite outro numero: "))
       print(" A soma dos numeros é: ", n1+n2)
    elif  ver=='-':
        n1 = float(input("digite um numero: "))
        n2 = float(input("digite outro numero: "))
        print(" A subtração dos numeros é: ", n1-n2)
    elif ver=='*':
        n1 = float(input("digite um numero: "))
        n2 = float(input("digite outro numero: "))
        print(" A multiplicação dos numeros é: ", n1*n2)
    elif ver== '/':
        n1 = float(input("digite um numero: "))
        n2 = float(input("digite outro numero: "))
        print(" A divisão dos numeros é: ", n1/n2)
    else:
        break;
    print("\n \n")
print("Terminou !!")
      
