#Elabore um programa Python que leia o peso ( em Kg)
#e a altura ou estatura alt (em metros) de uma pessoa,
#calcule e mostre o seu IMC (Índice de Massa Corpórea),
#sabendo que: imc = p/alt²

print("** Calculo IMC **")

peso = float(input("Digite o peso (Kg): "))
altura =  float(input("Digite a altura (m): "))

imc= peso/altura**2

print("Seu IMC é: ", round(imc,2))
