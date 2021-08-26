#Conversor de F para C

print("** Conversor de graus Fahrenheit para Celsius ** ")

f = float(input("Digite o grau em Fahrenheit: "))

c = (f-32)*5/9  # (f-32)/9 *5

print( round(f,2),"em Fahrenheit convertido para Celsius é: ", round(c,1))
