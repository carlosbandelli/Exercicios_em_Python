# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: carlos.vieira@aluno.faculdadeimpacta.com.br

#1
def eh_primo(n):
    tot = 0
    for c in range(1, n+1):
        if n % c == 0:
            tot += 1

    if tot == 2:
        return True
    else:
        return False



#2
def lista_primos(n):

    lp = []
    counter = 0
    for i in range(2, n+1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            lp.append(i)
            counter += 1
    lp.sort
    return lp




#3
def eh_perfeito(n):
    lista = []
    soma = 0
    for c in range (1, n):
        if n % c == 0:
            lista.append(c)
            soma += c
    if soma == n:
        return True
    else:
        return False
    lista.sort()
    return lista


#4
def perfeito(n):
    soma = 0
    for val in range(1, n):
        if n % val == 0:
            soma += val

    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista=[]
    for val in range(1, n + 1):
        if (perfeito(val)):
            lista.append(val)
    lista.sort()

    return lista




# 5
def eh_armstrong(n):
    tam = len(str(n))
    sum = 0
    div = n
    while div > 0:
        d = div % 10
        sum = sum + (d ** tam)
        div = div // 10
    if n == sum:
        return True
    else:
        return False




#6

def lista_armstrong(n):
    lista=[]
    for val in range(0, n + 1):
        if (eh_armstrong(val)):
            lista.append(val)
    lista.sort()
    return lista



#7
def eh_primo(x):
    if x < 2:
        return False
    else:
        for y in range(2, x):
            if x % y == 0:
                return False
        return True


def conta_primos(s):
    contador_primos = {}
    for numero in s:
        if eh_primo(numero):
            if numero in contador_primos:
                contador_primos[numero] += 1
            else:
                contador_primos[numero] = 1
    return contador_primos

def eh_quase_armstrong(n):
    tam = len(str(n))
    sum = 0
    div = n
    while div > 0:
        d = div % 10
        sum = sum + (d ** tam)
        div = div // 10
    if sum == n - 1:
        return (True)
    else:
        return (False)

