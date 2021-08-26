# Criamos uma lista com os valores digitados
#pelo usuário, visualizamos
# a lista e somamos todos seus valores.

resp = 's'
lista = [] #lista vazia
  
while resp == 'S' or resp == 's':
    try:
        n=float(input("Digite um numero: "))
        lista.append(n)
    # append por padrão coloca o novo elemento no final da lista
    #variavel.metodo() = lista.append()
    
    except:
        print("\n Digite somente numeros para a lista")
        #n=float(input("Digite um numero: "))

    resp = input("Deseja continuar a inserir (s/n): ")

print("A lista com os elementos digitados é: ", lista)

soma = 0

#len() função para saber o tamanho da lista
for i in range(len(lista)):
    soma =+lista[i]

print("A soma dos elementos da lista é: ", lista)





               
