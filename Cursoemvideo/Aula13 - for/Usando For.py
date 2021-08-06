for c in range (0,6): #se quiser que a contagem chegue até 6 ou voce acrescenta +1 ou coloca o ultimo numero pois ele sempre desconsidera um
    print('Oi')
print('Fim')

for c in range (1,6+1):
    print(c)

for c in range (6,0,-1): # dessa forma ele faz uma ocntagem regressiva
    print(c)

for c in range (0,7,2): # dessa forma ele faz uma contagem progressiva e pulando 2 em 2
    print(c)

n=int(input('Digite um número: '))

for c in range (0,n+1):# dessa forma definimos o final do laço
    print(c)
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in (i,f+1,p) #assim definimos o inicio o final +1(pois se nao tiver esse +1 ele ignora o ultimo numero e o passo
    print(c)
print('Fim')

for c in range(0,10) #dessa forma voce insere o valor 10 vezes e só escreve uma vez para isso
    n = int(input('Digite um valor: '))
print('Fim')

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s +=n
print(f'O somatório de todos od valores foi {s}')