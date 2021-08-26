#Cria e processa os dados dos automoveis digitados pelo usuario

resp = 's'
placas = []
precos = []
marcas = []
modelos = []

while resp == 's' or resp == 'S':
    try:
        pl = input("Digite a placa: ")
        placas.append(pl)
        pr = float(input("Digite o preço: "))
        precos.append(pr)
        mar = input("Digite a marca: ")
        marcas.append(mar)
        mod = input("Digite o modelo: ")
        modelos.append(mod)
    except:
        print("Digite valores validos")

    resp = input("Deseja cadastrar outro carro (s/n) : ")

soma = 0
qtde = 0
mpesq = input("Digite uma marca para pesquisar: ")
for i in range(len(marcas)):
    if marcas[i] == mpesq:
        soma += precos[i]
        qtde = qtde+1
try:
    print("A media de preços dos carros da marca ",
          mpesq," é: ",soma/qtde)
except:
    print("\n Não foi encontrado carros para a marca digitada",
          "\n Tente novamente mais tarde!!!!")
    



 


               
               
               
