#exemplo_4
#Solicita um número ao usuário e mostre os valores de sua
# tabuada.
#for

while True:
    print("** Programa Calcula tabuada ** ")

    num= int(input("Digite um numero inteiro para a tabuada: "))

    for t in range(1, 11):
        # range podemos valor inicial , valor final
        print(t, " * ", num, " = ", t*num)

    ver=input("deseja sair do programa (s/n): ")
    if ver =='s' or ver== 'S':
         break;
    print("\n \n")

print("Terminou !!")
    
