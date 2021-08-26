
resp = 's'

while resp == 's' or resp == 'S':# looping do programa
    print("Programa executando")# codigo do programa
    #quantas linhas quiser
    
    resp = input("Deseja continuar (s/n): ")
      #pergunta se deseja continuar
    
    while resp != 's' and resp !='n' and resp != 'S' and resp !='N' :
             print("opção invalida!!!!")
             resp = input("Deseja continuar (s/n): ")

    #if resp == 'N' or resp == 'n': # esse aqui é opção
       # break;
    
        
               
print("\n\n **** \n Sai do programa!!!!!")
