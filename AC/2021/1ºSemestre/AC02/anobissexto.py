ano= int(input())
anof= int(input())
counter = 0
for i in range(ano, anof +1):
    if (i%4==0 and i%100!=0) or (i%400==0):
        print(i)
        counter += 1
print('bissextos: {}'.format(counter))
