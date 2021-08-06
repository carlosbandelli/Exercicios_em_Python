#posicionamento de listas
pessoas= [['pedro',25],['maria',19], ['João',32]]
print(pessoas[0][0]) #mostra a posição 0 dentro da posição 0
print(pessoas[1][1]) #mostra a posição 1 dentro da posição 1
print(pessoas[2][0]) #mostra a posição 0 dentro da posição 2
print(pessoas[1]) #mostra o que tem dentro da chave 1
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
galera = [['Joao',19],['Ana',33],['joaquim', 13], ['Maria', 45]]
print(galera[0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
galera = list()
dado = list()
totmai = 0
totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # criar copia [:]
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é menor de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')