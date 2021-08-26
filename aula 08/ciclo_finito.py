# ciclo finito ele vai ser interrompido
#por uma ação do usuario

print(" ** Ciclo Finito **")
print("Para encerrar o programa digite a palavra 'fim'")

while True:
    nome=input("digite o nome: ")
    if nome == "fim":
        break
    print("o nome digitado é :",nome)

print("O programa terminou \n ehhhhh!!!!")

