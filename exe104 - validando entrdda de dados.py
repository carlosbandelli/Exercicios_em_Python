def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero inteiro válido.')
        if ok:
            break
    return valor


#program principal
n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')