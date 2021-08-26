#elabore um programa Python que leia o valor do raio (r) de um cilindro
#e sua altura (h),
#calcule e visualize a área da base (Ab) e seu volume (V), sendo:    
#V= Ab*h
#Ab = pi r²

#pi = 3,24
#math.pi

import math

print("Calculo de colume e area da base de um cilindro")

r = float(input("Digite o valor do raio: "))
h = float(input("Digite a altura: "))

ab = math.pi * r**2

v= ab*h

print("A area da base do cilindro é: ", round(ab,2),
      "\nO volume é: ",round(v,2))



