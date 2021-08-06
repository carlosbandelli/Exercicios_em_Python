num = [2,5,9,1]
num[2] = 3 #<--- altera o valor da listo pelo valor atribuido
num.append(7)# <--- adiciona na no final da lista
num.sort()# <---- organiza a lista
num.insert(2,0)#<--- serve para adicionar os valores na posiçao que voce quiser, nesse caso 1º a posição (2) e depois o valor (0)
print(num)
num.sort(reverse=True) #<----- faz o reverso da lista
print(num)
print(f'Essa lista tem {len(num)} elementos.') #<--- mostra o tamanha da lista
del num[1]
num.pop()#<---sem parametro ele removo o ultima posição
num.pop(2)#<----- com parametro ele elimina a posição, quando o parametro é dado
#Exemplo
if 4 in num: #quano não tem o numero
    num.remove(4)
else:
    print('Não achei o número 4')
# Posso começar um alista vazia de duas maneiras
# valores = list()
# ou essas forma mais facil
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores): #dessa forma mostra os numeros e sua posição da chave
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2,3,4,7]
b = a[:] #criou um copia de a para b, se a recebe-se b sem esse parametro ele faria uma ligação
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')