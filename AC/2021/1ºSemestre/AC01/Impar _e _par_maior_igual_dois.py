
## Funções##
def pede_idade(mensagem):
    numero = input(mensagem)
    numero = int(numero)
    return numero
## Código principal ##
numero  =  pede_idade('')


if numero % 2 == 0:
    Numimp = int( numero - 1)
    Numpar = int(numero + 2)
    print( Numimp , Numpar )
    
else:
    Numimp = int( numero - 2)
    Numpar = int(numero + 1)
    print(  Numimp , Numpar)
