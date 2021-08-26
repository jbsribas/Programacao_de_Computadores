# Criamos uma lista com valores fixos,
#visualizamos a lista, visualizamos
# o primeiro e o último elemento da lista,
#somamos os valores da lista e
# visualizamos os elementos nas posições pares.

lista = [4.0, 9.2, 3.1, 9.1, 1.5, 3.2, 2.6]

#visualizar a lista
print("A lista criada é: ", lista)

#visualizar primeiro elemento
print("O primeiro elemento da lista:",lista[0])

#visualizar ultimo elemento
t = len(lista)

print("O ultimo elemento da lista:", lista[t-1])

#somarmos os valores da lista
somaF = sum(lista)
print("a soma com a função sum", somaF)

somaC = 0
for i in lista:
    somaC = somaC +i

print("A soma acumulada com for", somaC)


somaC=0
j = 0
while len(lista)>j:
    somaC = somaC+lista[j]
    j = j+1

print("A soma acumulada com while", somaC)

#visualizamos os elementos nas posições pares.

print("Exibe elementos indice par com while: ")
c = 0
while len(lista)>c:
    if c%2 == 0:
        print(lista[c])
    c = c+1

print("exibe elementos indice par com for: ")
for i in range(0,len(lista),2):
         # lista de 0 até o tamanho da lista, de ++2    
    print(lista[i])   


    



