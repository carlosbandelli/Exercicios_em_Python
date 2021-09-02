def eh_amrstrong(n):
    tam = len(str(n))
    sum = 0
    div = n
    while div > 0:
        d = div % 10
        sum = sum + (d ** tam)
        div = div // 10
    if n == sum:
        return (True)
    else:
        return (False)
def lista_amrstrong(n):
    lista=[]
    for val in range(1, n + 1):
        if (eh_amrstrong(val)):
            lista.append(val)
    lista.sort()
    return lista

x = lista_amrstrong(93084)
print(x)