#IMC básico

print("** Calculo IMC **")

peso = float(input("Digite o peso (Kg): "))
altura =  float(input("Digite a altura (m): "))

imc= peso/altura**2

print("Seu IMC é: ", round(imc,2))
