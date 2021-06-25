'''co = float(input('Compirmento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacent: '))
hi = (co**2 + ca**2)**(1/2)
print(f'A hipotenuso vai medir {hi:.2f}')'''
import math
co = float(input('Compirmento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacent: '))
hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hi:.2f}')
