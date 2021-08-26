#exemplo 5 - imc com try / except

try:
    peso=float(input("Digite o peso da pessoa (Kg): "))
    altura = float(input("Digite a altura da pessoa (m): "))
    imc= peso / altura**2
    print("O IMC é: ",imc, "Kg/m**2")
except:
    print("\nO peso e a altura são valores númericos")
    print("Digite as casas decimais utilizando ponto (.)")
    print("Tente executar ese programa novamente...")

print("\n \n O programa continua a execução normalmente")
          
