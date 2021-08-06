n = s = 0
while True:# nesse caso p break é usado para interromper o loop sem somar
    n = int(input('Digite um número: '))
    if n == 999:# quando o usuario fazer esa condição o programa para e soma os valores qeu foram inseridos
        break
    s += n # aqui ele soma os valores sem somar a condição
print(f'A soma vale {s}')