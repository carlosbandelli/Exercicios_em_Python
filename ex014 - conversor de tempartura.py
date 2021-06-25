celsius = float(input('Temperatura em ºC: '))
F = (celsius * 9/5) + 32
if celsius == -273.15:
    print(f'Parabens voce alcançou o zero absoluto, que em Fahrenheit é {F:.2f} ºF ')
else:
    print(f'Sua temperatura {celsius:.2f} ºC para Fahrenheit é {F:.2f} ºF')
