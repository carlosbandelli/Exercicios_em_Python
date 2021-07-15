def notas(*n, sit=False):
    """
    -> Função para analisar a notas e situações de varios alunos
    :param n: uma ou  mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adiconar a situação.
    :return: dicinário com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÀVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)