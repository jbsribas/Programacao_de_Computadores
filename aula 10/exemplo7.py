# exemplo 7

# calcular num procedimento o seno, cosseno e tangente
#de um angulo em graus

# importações das bibliotecas
import math

# definição dos metodos
def calcula(ang):
    #as funções sin, cos e tan esperam o valor
    #do angulo em radianos,
    #por isso se faz necessario converter
    ang = math.radians(ang)
    print("angulo em radianos: ", round(ang,2))
    print("seno: ", round(math.sin(ang),2))
    print("cosseno: ", round(math.cos(ang),2))
    print("tangente: ",round(math.tan(ang),2))


# chamada do procedimento / método sem retorno

angulo = float(input("Digite o angulo em graus: "))
calcula(angulo)

