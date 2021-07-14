def área(larg, comp):
    a = larg * comp
    print(f'A Area d eum terrno {larg}x{comp} é de {a}m².')

# Programa principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)