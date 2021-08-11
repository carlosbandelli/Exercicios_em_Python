# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: carlos.vieira@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    tot = 0
    for c in range(1, n+1):
        if n % c == 0:
            tot += 1

    if tot == 2:
        print(True)
    else:
        print(False)

eh_primo(7)

def lista_primos(n):
    """Função que retorna uma lista de primos até n
    Recebe um número natural n, com n >= 2, e retorna uma
    lista com todos o números primos estritamente menores
    que n, em ordem crescente.
    Parâmetros
    ----------
    n : int
    Número natural que define o limite superior da lista.
    Retorno
    -------
    list
    itens : int
    descrição : Lista com todos os números primos menores
    que n, em ordem crescente.
    """
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
    print(lp)

lista_primos(7)



def eh_perfeito(n):
    soma = 0
    for c in range (1, n):
        if n % c == 0:
            soma += c
    if soma == n:
        print(True)
    else:
        print(False)

eh_perfeito(6)