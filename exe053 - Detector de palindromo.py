frase = str(input('Digite uma frase: ')).strip().upper() #strip elimina os espaços antes e depois da frase
palavras = frase.split()#splitei para gerar uma lista( vetor)
junto=''.join(palavras)# juntei alista para eliminar o epaços antes
inverso = ''
for letra in range(len(junto)-1,-1,-1): # usei o len para ir da ultima letra ate a primeira
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')