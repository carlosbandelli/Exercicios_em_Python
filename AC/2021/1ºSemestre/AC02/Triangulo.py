import string
a = list(string.ascii_uppercase)
n = int(input())

for i in range(1,n+1):
    print (a[i-1]*i)