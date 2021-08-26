#Faça um programa em Pyhton que leia um número digitado
#pelo usuário. Se este for maior que 8, calcular a divisão por 2
#do valor, senão (se for menor ou igual que oito) calcular o
#cubo do valor. Visualize o resultado em cada caso.

num = int(input(" Digite um numero inteiro: "))

if num > 8:
    print(num,"/2 = ",num/2)
    
else:
    print(num," **3 = ", num**3)
