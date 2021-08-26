#criar as quatros listas com dados fixos

placas = ['ABC-1234','DEF-4567','CDE-4321','WXY-2121','AAA-1112']
precos = [25000,75000,50000,200000,15000]
marcas = ['Fiat','Ford','Fiat', 'Audi','vw']
modelos = ['Uno','Focus','Palio','A6','Fusca']

print("Dados cadastrados: ")
print(placas, "\n", precos, "\n", marcas, "\n", modelos, "\n")

#Calcular a média  dos  preços  dos carros  de marca digitados
#usuário:

soma = 0
qtde = 0
mpesq = input('Digite  uma marca para  pesquisar: ')

for i in range(len(placas)):
    if marcas[i] == mpesq:
        soma += precos[i]
        qtde = qtde +1

print("A média de preços do carros da marca", mpesq,
      " é ",soma/qtde,"\n")

#Listar os carros com preços abaixo de 55000.00
print("os carros com preço abaixo de R$55000.00: ")

for j in range(len(placas)):
    if precos[j] < 55000:
        print(placas[j],precos[j],marcas[j],modelos[j])


#determinar o carro cadastrado mais barato
menor = 99999999999
pos = -1

for k in range(len(placas)):
    if precos[k] < menor:
        menor = precos[k]
        pos = k

print("O carro mais barato é: ",placas[pos],
      " R$ ",precos[pos],marcas[pos],modelos[pos])
         


    

