teste = "a linda casa verde" # isso é uma String

print("tamanho", len(teste))

print("countando a quantidade de a ",teste.count("a"))

varA= "A vida"
varB = "é bela"
varC = varA+" "+varB # concatenação (junção) de string

print(varA)
print(varB)
print(varC)

var1 = " a gota d'água "
print(var1)

var2 = ' segundo fulano de tal " A vida deve ser vivida"'
print(var2)
print(var1+ var2)

print("Quantidade da palavra casa:",teste.count("casa"))

print("posição da palavra linda",teste.find("feia")) #buscar


print(teste.split(" ")) # cortar / dividir

print(teste.split("casa"))

print(teste.upper()) # todas as letras em maiusculos

print(teste.lower()) # todas as letras em minusculo

print(teste.capitalize()) # a primeira letra em maiusculo

print(teste.title()) # todas as primeiras letras das palavras

teste = teste.upper()
print(teste)

# uma substring é quando pegamos um trecho da string
#pela manipulação dos indices

umastring = "uma casa"
print("substring",umastring[1:5])

string = "quase amarelo"

for i in range(6,10,1):
    print(string[i])

print("\n\n")

for i in range(len(string)):
    print(string[i])
print("\n\n")

for i in range(len(string)-1,-1,-1):
    print(string[i])










