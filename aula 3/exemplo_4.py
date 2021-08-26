#Escreva um algoritmo (programa Python) para
#ler o salário mensal  de um funcionário
     #e o percentual de reajuste
#Calcular e visualizar o valor do novo salário

salarioMensal = float(input("Digite o salario do funcionario: "))
reajuste = float(input("Digite o percentual de reajuste: "))
percentual = reajuste/100
novoSalario = salarioMensal+(salarioMensal*percentual)
print(" o valor a ser incrementado no salario atual é",
                           (salarioMensal*percentual))
print("o NOVO salario calculado é: ",novoSalario)

### 

