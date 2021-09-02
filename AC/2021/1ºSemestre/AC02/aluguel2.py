divida = int(input())
pagar = int(input())
counter = 1
for antes in range(divida, 0, - pagar):
    depois = antes
    if depois < pagar:
        antes = 0
    else:
        antes -= depois
    print('pagamento: {}'.format(counter))
    print('antes  = {}'.format(depois))
    print('depois = {}'.format(antes))
    print('-' * 5)
    counter += 1