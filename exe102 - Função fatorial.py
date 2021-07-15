def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um Número
    :param n: O número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa Principal
print(fatorial(5, show=True))
help(fatorial)