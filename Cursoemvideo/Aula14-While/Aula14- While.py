'''for c in range(1,10):
    print(c)
print('Fim')'''

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

# WHILE é usado quando voce não sabe o final, agora o for é quando voce ja sabe

n = 1
while n != 0:
    n = int (input('Digite um valor: '))
print('Fim')
# Nesse caso abaixo usando while pois não sei quando o usuario irá escrever N, ou seja não seio final
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

# mais uma aplicação de while

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n !=0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares! ')