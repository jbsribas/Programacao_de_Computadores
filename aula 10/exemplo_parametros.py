# exemplos da utilização de parametros / argumentos

#Definição dos metodos a serem utilizados 
def metodoA(lista): #recebe como parametro uma lista
    lista[0]= 9
    # alterou o valor de um indice ou elemento da lista
    lista[2] = 99

def metodoB(vSimples):
    vSimples = 88 # variavel local só existe dentro do metodo

def metodoC(vSimples):
    vSimples = "janela" # variavel local só existe no metodo


# utilização / chamada dos metodos

minhalista=[4,3,6,7,8] # variaveis globais
print("antes :" ,minhalista)
metodoA(minhalista)
print("depois :" ,minhalista)

variavelA=6 # variavel global 
print("antes: ", variavelA)
metodoB(variavelA)
print("depois: ", variavelA)

variavelB = "casa" # variavel global
print("antes: ", variavelB)
metodoC(variavelB)
print("depois: ", variavelB)

# para proteger o valor das variaveis globais
#não é permitido a alteração delas por procedimentos
#metodos sem retorno.
# caso seja necessario alterar o
#valor utilize uma função (metodo com retorno)
# variavelA = metodoD(variavelA)
# porém como visto no exemplo a
#integridade da lista foi alterada no metodoA (vulgo procedimento)
# isso ocorreu porque no código a alteração é diretamente
#no indice/elemento da lista (vulgo subvariavel)
#pois no metodoA não tentou mudar o valor da lista como um todo
# lista = ""
# lista = " qualquer valor)
# mante-se a estrutura original em lista
#e alterou dois indices






            
