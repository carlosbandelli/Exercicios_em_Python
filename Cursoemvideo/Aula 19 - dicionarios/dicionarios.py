pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) # OS nomes da chaves
print(pessoas.values()) # mostra os valores da chaves
print(pessoas.items()) # mostra tanto as chaves quantos os valores
for k in pessoas.keys():
    print(f' só mostro as chaves: {k}')

for k in pessoas.values():
    print(f'Só mostros os valores dentro das chaves: {k}')

for k, v in pessoas.items():
    print(f'Mostro ambos a chave {k} e o valor {v}')

pessoas['nome'] = 'Leandro' # Assim posso atribuir o valor ou alterar o valor que esta na chave
pessoas['peso'] = 98.5 #atribuindo chave com valores
print(pessoas)

#``` Criando Dicionario dentro de uma lista```
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil) # mostra o que tem na lista
print(brasil[0]) # mostra oq ue tem na chave 0
print(brasil[0]['uf']) # mostra a chave dentro da chave
print(brasil[1])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # esse é o tedo usado apra copiar em dicionario
for e in brasil: # for da lista
    for k, v in e.items(): # for para os valores do dicionarios
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

