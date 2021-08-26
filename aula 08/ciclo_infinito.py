# ciclo infinito

n=10

while True:
    #print(n)
    n=n-1
    if(n%2 == 0):
       print('0',end="\t")
    else:
        print('1',end="\t")  
    if(n==11):
# exemplo com uma condição que não pode ser satisfeita
       break

#fora do looping
print("O programa terminou \n ehhhhh!!!")



