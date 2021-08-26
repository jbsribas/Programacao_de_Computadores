print("** Calendario - 4**")
dia = int(input("Digite o dia: "))
mes = int(input("digite o mes: "))
ano = int(input("digite o ano: "))
mesl= " "

if dia >=1 and dia<= 31 and mes >=1 and mes <=12:
      if mes==1:
          print("A data é ",dia," de janeiro de ",ano)
      elif mes==2 and dia <=29:
           print("A data é ",dia," de fevereiro de ",ano)
      elif mes==3:
           print("A data é ",dia," de março de ",ano)
      elif mes==4 <=30:
           print("A data é ",dia," de abril de ",ano)
      elif mes==5:
           print("A data é ",dia," de maio de ",ano)
      elif mes==6 <=30:
           print("A data é ",dia," de junho de ",ano)
      elif mes==7:
           print("A data é ",dia," de julho de ",ano)
      elif mes==8:
           print("A data é ",dia," de agosto de ",ano)
      elif mes==9 <=30:
           print("A data é ",dia," de setembro  de ",ano)
      elif mes ==10:
          print("A data é ",dia," de outubro de ",ano)
      elif mes == 11 <=30:
          print("A data é ",dia," de novembro de ",ano)
      elif mes==12:
          print("A data é ",dia," de dezembro de ",ano)
      else:
          print("data invalida para esse mes e dia")
else:
    print("dia ou mês invalido")






    
