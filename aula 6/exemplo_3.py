#exemplo 3 

#Em uma escola, um aluno aprovará uma disciplina se
#a média das três avaliações for maior ou igual que 6
#e o percentual de presença maior ou igual que 75
#Também aprovaria se a média for maior que 8 independente
#da frequência Em qualquer outro caso o aluno estará reprovado

nota1 = float(input("Digite a nota 1: "))

nota2 = float(input("Digite a nota 2: "))

nota3 = float(input("Digite a nota 3: "))

freq = float(input("Digite o percentual de presença:"))

media = (nota1+nota2+nota3)/3

if media >= 6 and freq >= 75:
       print("O aluno foi aprovado")

elif media >= 8:
       print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")






    
