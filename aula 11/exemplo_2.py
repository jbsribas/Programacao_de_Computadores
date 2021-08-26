#exemplo_2
#append(): insrção na lista no final
#len(): tamanho da lista

#quero inserir um elemento na lista
#numa posição especifica

l = ["Java","MySql","Python","Oracle","CSS"]

for i in l: #percorrer a lista
    print(i)

print("tamanho lista ",len(l))

l.insert(3,"HTML") #inserir em uma posição determinada

print(l,"tamanho",len(l))

#remover o ultimo elemento da lista
l.pop()
print(l,"tamanho",len(l))

#remover um elemento de indice especifico
l.pop(0)
print(l,"tamanho",len(l))

#remover item da lista pelo conteudo do elemento
l.remove("Python")
print(l,"tamanho",len(l))

#ordenar de maneira crescente
l.sort()
print(l,"tamanho",len(l))

#ordernar de ordem decrescente
l.reverse()
print(l,"tamanho",len(l))


#Verficar o valor minimo e maximo de uma lista

v = [1,10,101,6,7.3,9,-8,10]

print("menor valor da lista: ",min(v))
print("maior valor da lista: ", max(v))
print("conheça toda a lista: ", v)

#contar
print("ocorrencia do numero 10: ",v.count(10))




