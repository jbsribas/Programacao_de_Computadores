print("** Calendario - 3**")
dia = int(input("Digite o dia: "))
mes = int(input("digite o mes: "))
ano = int(input("digite o ano: "))
mesl= " "

if dia >=1 and dia<= 31 and mes >=1 and mes <=12:
      if mes==1:
          mesl="janeiro"
      elif mes==2:
          mesl= "fevereiro"
      elif mes==3:
          mesl="março"
      elif mes==4:
          mesl="abril"
      elif mes==5:
          mesl="maio"
      elif mes==6:
          mesl="junho"
      elif mes==7:
          mesl="julho"
      elif mes==8:
          mesl="agosto"
      elif mes==9:
          mesl = "setembro"
      elif mes ==10:
         mesl ="outubro"
      elif mes == 11:
         mesl="novembro"
      else:
         mesl = "dezembro"
      print("A data é ",dia," de ",mesl," de ",ano)
else:
    print("dia ou mês invalido")






    
