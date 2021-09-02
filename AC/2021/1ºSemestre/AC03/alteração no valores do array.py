n = int(input())
p = []
at = []
nf = []
cont= 0

for i in range(n):
    p.append(float(input()))
for j in range(n):
    at.append(float(input()))
for k in range (n):
    if p[k] == 10 or at[k] !=10:
       nf.append(p[k])
    elif at[k] == 10:
       nf.append(p[k]+2)
       cont +=1
       if nf[k] >10:
         nf[k] = 10
         nf.append(k)


print(F'NOTAS ALTERADAS: {cont}')
for pr in range (n):
    if p[pr] == 10 or at[pr] != 10:
        print(f'-(00{pr+1}) original: {p[pr]:05.2f} | final: {nf[pr]:05.2f}')
    else:
        print(f'*(00{pr+1}) original: {p[pr]:05.2f} | final: {nf[pr]:05.2f}')