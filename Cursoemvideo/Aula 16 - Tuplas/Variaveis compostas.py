# em python para difernciar listas de tuplas e dicionarios
# usasse () <- representa tupla
# [] <- representa lista
# {} <- representa dicionario
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#negativo      -4          -3       -2      -1
print(lanche[3]) #mesmo sendo tuplas se referencia com [] igual lista
print(lanche[-2])
print(lanche[1:3])# ele só mostra o 1 e o 2, ele semore discarta o ultima numero
print(lanche[2:])# do lelemento do 2 até o final
print(lanche[:2])# me mostre do inicio até elemnto 2, lembrando que vai ignoarra o ultimo elemento mostradno então o 0 e 1
print(lanche[-3:]) #me mostra no -3 ate o final
print(lanche)#mostra a tuplas inteira
#tuplas são imutáveis
#lanche[1] = 'Refrigerante'
#print(lanche[1])

for comida in lanche:
    print(f'EU vou comer {comida}')
print('Comi muito!')
for pos,comida in enumerate(lanche): #uso diretamento minha variavel composta, enumerate mostra a posição , porem temos que acrescentar mais uma variavel
    print(f'EU vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print(len(lanche))# Esse comando serve para verifica o tamanho da tupla
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batat-frita')
for cont in (0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição{cont}') #mostra o lanche qu esta dentro da posição cont, e o outro cont mostra a chave que esta
print('Comi pra caramba')
print(sorted(lanche)) #colocar em ordem
print(lanche)

a=(2,5,4)
b=(5,8,1,2)
c = a + b
print(c)
print(len(c))
print(c.count(5))# ele conta quantas vezes aparece o numero porposto
print(c.index(8))# ele mostra em que posição esta o numero proposto, porem ele só mostra a priemira ocorrencia
print(c.index(5,1)) #parametros primeiro o numero que voce quer e aposição que ele começa a contagem
pessoa = ('Gustavo', 39, 'M', 99.88)# tuplas heterogeneas
print(pessoa)





