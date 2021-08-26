#exemplo 7
# try/except

try:
    peso= float(input("Digite o seu peso (em KG): "))
    altura = float(input("Digite sua estatura (em m): "))
    imc = peso/altura**2
    print("Seu IMC é ", imc," KG/m**2")

except:
    print("Por favor digite os valores corretos")

