# exemplo 6 - calcular media e  fatorial por função

#definir as funções

def media(a,b):
    return((a+b)/2)

def fatorial(n):
    prod = 1
    
    for j in range(1,n+1):
        prod = prod *j

    return prod


# chamada das funções / metodos no código

x = float(input("Digite o 1° valor: "))
y = float(input("Digite o 2º valor: "))
print("A média vale: ",media(x,y))

k = int(input("Digite um valor inteiro: "))
print("O fatorial de ", k," é: ",fatorial(k))


        
