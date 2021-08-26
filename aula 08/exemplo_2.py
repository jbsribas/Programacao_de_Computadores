#exemplo_2
#Leia 10 números inteiros e calcular/mostrar a soma dos
#números pares.

somaPar=0 #acumulador

for i in range(10):
    n=int(input("Digite um numero inteiro: "))
    if n%2 == 0: #% resto da divisão
        somaPar = somaPar+n;
        #o ponto e virgula não é obrigatório mas pode colocar
        
print("A soma de todos os numeros pares é: ", somaPar)




