def verificarC(r):
    while r.upper()!='S' and r.upper()!= 'N':
          print("Valor incorreto, tente novamente")
          r = input("Deseja continuar incluindo (s/n): ")

    return(r)

def verNota(nota):
    while True:
             if nota> 5:
                 print("valor incorreto!",
                  "\nAs notas devem ser menor igual a 5")
                 nota=float(input("Digite a nota mais uma vez: "))
             else:
                 break;
    return nota

############################################################
#criar lista vazias
nome = []
g = []
a1 = []
a2 = []
a3 = []
af = []
maior = 0
#laço de repetição para o cadastro dos alunos
resp = 'S'
while resp.upper() == 'S':
    try:
         nome.append(input("Nome do aluno: "))
         g.append(input("Genero: "))
         
         # verificação e as notas são menores ou igual a 5
         n = float(input("Digite a A1: "))
         n = verNota(n)
         a1.append(n)
          
         n = float(input("Digite a A2: "))
         n = verNota(n)
         a2.append(n)
          
         n = float(input("Digite a A3: "))
         n = verNota(n)
         a3.append(n)

         
         u =  len(nome)-1
         if a2[u] > a3[u]:
             maior = a2[u]
         else:
             maior = a3[u]
             
         af.append(float(a1[u]+maior))
         print("A NF é: ", af[u])
    
    except ValueError:
        if len(nome) > -1: # se a lista não estiver vazia
             nome.pop() # remove o ultimo elemento da lista
             if len(g)> len(nome):
                 g.pop()
             if len(a1) > len(nome):
                 a1.pop
             if len(a2) > len(nome):
                 a2.pop
             if len(a3) > len(nome):
                 a3.pop
             if len(af) > len(nome):
                 af.pop
        print("Digite apenas numeros")
         
    resp = input("Deseja continuar incluindo (s/n): ")
    resp = verificarC(resp)

   

#-- parte depois da inclusão

#aluno com maior Nota final
verM = -1
indice = -1

for i in range(len(af)):
    if af[i] > verM:
        verM = af[i]
        indice = i
try:
    print("\n Aluno(a) com a maior nota final: ",nome[indice],
              "\nSexo: ",g[indice],
              "\nNota Final: ",af[indice])

except IndexError:
     print("lista vazia")


# aluna com menor nota final
menor = 9999999999
indice = -1

for i in range(len(g)):
    if g[i].upper() == 'FEMININO' or g[i].upper() == 'F':
        if af[i] > menor:
            menor = af[i]
            indice = i
try:
    print("\nA aluna com menor nota: ",nome[indice],
              "\nNota Final: ",af[indice])

except IndexError:
     print("lista vazia")

# contar alunos reprovados
reprovados = 0

for i in range(len(af)):
    if af[i] < 6:
        reprovados = reprovados + 1
    

print("A quantidade de alunos reprovados é: ", reprovados)



          
          
