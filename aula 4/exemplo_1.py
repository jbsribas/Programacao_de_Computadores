#Aula 04 - exemplo_1

###############################################
import math

###############################################
angulo = float(input("digite o valor do angulo alpha"
                     +" em radianos: "))

seno = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print("o valor em radianos de seno, cosseno e tangente para o"
      +"angulo ",angulo, "é: \n *",seno, "\n *",cos,
       "\n *",tan, "\n\n")

print("valores ajustados: \n *** seno ",round(seno,4),
       "\n *** cos ",round(cos,4), "\n *** tan ", round(tan,4))  

#\n dentro de uma string significa quebra de linha
print("\n \n quero pular de \n linha e "
      +"também quero \t tabular (tabulação) texto")








