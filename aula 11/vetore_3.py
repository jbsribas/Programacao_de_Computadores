# Criamos uma lista com valores pares, começando em 2.
#O usuário digita o número final para parar a inserção
#na lista.
resp = 's'
while resp =='s' or resp =='S':
    try:
        n = eval(input("Digite um numero final: ")) #int()

#eval = valor numerico float ou int e sim um numero
#evaluation

        lista = [] #lista vazia

#o looping começa com 2
#vai até n pq n+1 é o criterio de parada,
#incrementa de 2 em 2 ou seja ++2
        for k in range(2,n+1,2):
            lista = lista+[k]# adicionamos uma lista de um elemento [k]

        print(lista)
    except:
        print("Digite um numero inteiro!!!!!!!")

    resp=input("Deseja continuar (s/n): ")

print("Terminou!!!!!")



