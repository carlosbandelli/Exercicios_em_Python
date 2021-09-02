lista = []
soma = 0
cont = 0
while True:
    l = int(input())
    if l < 0:
        break
    lista.append(l)
    soma += l
    cont +=1
media = soma / cont
print(f'MEDIA: {media:.2f}')
for n in lista:
    if media > n:
         print(n)