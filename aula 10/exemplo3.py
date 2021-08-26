# exemplo3 IMC com ciclo

n = int(input("Digite a quantidade de pessoas processadas? "))

for i in(0,n):
    peso=float(input("Digite o peso da pessoa (Kg): "))
    altura = float(input("Digite a altura da pessoa (m): "))
    if (peso > 0 and altura > 0.10 and altura < 2.5):
        imc= peso / altura**2
        print("O IMC é: ",imc, "Kg/m**2")
    else:
        print("Verifique por favor, valor incorreto!!!")

print("\n até logo!!!!!")

