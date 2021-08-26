#Exemplo1 - listas

listaA = ['verde',"cinza","amarelo","azul"]
listaB = [12,31,4,21,3,120,32]
listaC=['verde','cinza',100,230,4.3]

print("tamanho lista A: ",len(listaA))
#len: função de tamanho da lista

for i in listaA:
    print(listaA)
    print(i)

print("percorrer lista A com while")
j = 0
while len(listaA) >j:
    print(listaA[j])
    j= j+1



listaV = [] #lista vazia
print("lista vazia ",len(listaV), listaV)
