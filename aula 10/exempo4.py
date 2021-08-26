# exemplo 4  IMC com ciclo -  while

resp = 's'
while resp == 's':
    peso=float(input("Digite o peso da pessoa (Kg): "))
    altura = float(input("Digite a altura da pessoa (m): "))
    if (peso > 0 and altura > 0.10 and altura < 2.5):
        imc= peso / altura**2
        print("O IMC é: ",imc, "Kg/m**2")
    else:
        print("Verifique por favor, valor incorreto!!!")

    resp = input("\n Deseja continuar (s/n) ? ")

print("\n até logo!!!!!")
