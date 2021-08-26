# exemplo 2 IMC com metodo

# Metodo com retorno é chamado de função
# metodo sem retorno é procedimento
#para criar o metodo nos usamos a palavra reservada def

#ele pode ter argumento (parametro) ou não ()

#metodo com argumento e retorno (função / function)
def imc(p,a): #argumento ou parametro só existe dentro do metodo por isso
    calc = p / a**2 # apos os calculos ou verificação se faz necessario
    return(calc) #  o uso do return


#metodo sem argumento e sem retorno (procedimento / procedure)
def despedida():
    print("Obrigada por utilizar este programa")
    print("Até logo")

peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))

print("O IMC calculado é: ", imc(peso,altura), "Kg/m**2")
despedida()



