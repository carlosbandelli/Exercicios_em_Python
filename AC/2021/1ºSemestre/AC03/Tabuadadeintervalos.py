a = int(input())
b = int(input())
tab = a
if tab > b :
    print('Nenhuma tabuada no intervalo!')

while tab <= b :
    i=1
    while i <= 10:
       print(f'{tab} x {i} = {tab*i}')
       i=i+1

    tab += 1
    print('-' * 10)

