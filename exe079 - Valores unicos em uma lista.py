numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitour os valores {numeros}')
