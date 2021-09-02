qtdV = 0
valorR = 0
n = float(input())
while n != -1:
    qtdV += n
    valorR = qtdV *2.50
    n = float(input())
print(f'VC$ {qtdV:.2f}')
print(f'R$ {valorR:.2f}')
