#Aula 04 exemplo_02

####################################

import math

######################################
angulo = float(input("digite o angulo alfa em Graus: "))

#math.degrees(x), math.radians(x)

anguloR = math.radians(angulo)
seno = math.sin(anguloR)
cos = math.cos(anguloR)
tan = math.tan(anguloR)

print("o resultado em radianos do angulo alpha é ", anguloR)
print("o seno de alpha é ", seno)
print("o cos de alpha é ", cos)
print("a tan de alpha é ", tan)
print("\n\n")
print("o resultado em graus do angulo alpha é ", angulo)
print("o seno de alpha é ", math.degrees(round(seno)))
print("o cos de alpha é ", math.degrees(round(cos)))
print("a tan de alpha é ", math.degrees(round(tan)))

 
