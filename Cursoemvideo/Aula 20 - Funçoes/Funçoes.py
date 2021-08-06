# * significa desempacotar
# Olha o cara vai passar variso parametros aqui, eu nao sei quantos são, voce vai pegar todos esse aparemtros e jogar dentro de num

def contador(* num):
    for valor in num:
        print(valor, end='')
    print('FIM !')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra (lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2 #a posição da lista recebe ela vezes 2
        pos +=1
valores = [6, 3, 9, 1 ,0, 2]
dobra(valores)
print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4)