inicio= int(input(''))
fim = int(input(''))
counter = 0
for i in range(inicio, fim +1):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        print(i)
        counter += 1
print('primos: {}'.format(counter))

