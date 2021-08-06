# Criando uma lista dentro de um for.
#Vejamos agora como criar uma lista dentro de um laço de repetição.
# No exemplo abaixo, começamos com uma lista de frutas e desejamos
# criar uma lista com os nomes dessas frutas no plural.
# Vejamos uma forma de se fazer isso:
frutas = ['laranja', 'banana', 'abacate', 'manga']
plurais_frutas = []
for fruta in frutas:
    plural = fruta + 's'
    plurais_frutas += [plural]
print(plurais_frutas)