#calculo salario

# entrada
ht= float(input("Digite as horas trabalhadas no mês: "))
vh= float(input("Digite o valor hora trabalhada: "))
pd = float(input("Digite o percentual de desconto: "))


#processamento

sb=ht*vh
td = (pd/100)*sb
sl= sb-td

# resultados/ saída

print("A quantidade de horas trabalhadas este mês é: ",ht,
      "\nO salário bruto é: ",round(sb,2), "\nO desconto total é: ",round(td,2),
      "\nO salário liquido: ", round(sl,2))

