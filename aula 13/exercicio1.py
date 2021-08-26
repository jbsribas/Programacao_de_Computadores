resp = 'S'
while resp.upper() == 'S':
    placas = ['ABC-1234', 'DEF-4567', 'CDE-4321',
              'WXY-2121', 'AAA-1112']
    precos = [30000, 75000, 50000, 200000, 15000]
    marcasmod = ['Fiat Uno', 'Ford Fiesta', 'Fiat Argo',
             'Audi A4', 'VW Fusca']

    soma = 0
    qtde = 0

    mpesq = input("Digite uma marca para pesquisar: ")

    for i in range(len(placas)):
        if marcasmod[i].upper().find(mpesq.upper())>=0:
            soma += precos[i]
            #soma = soma + precos[i]
            qtde = qtde+1

    if qtde >0:
        print("A média de preço  dos carros  da marca", mpesq,
              " é ",soma/qtde)
    else:
        print("Não encontramos o automóveis dessa marca", mpesq)

    resp = input("Deseja continuar a execução (s/n): ")
    
    while resp.upper() != 'S' and resp.upper()!='N':
        print("Opção incorreta!! ")
        resp = input("Deseja continuar a execução (s/n): ")
        


        
