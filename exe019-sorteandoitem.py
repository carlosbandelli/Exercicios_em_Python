import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista =[n1, n2, n3, n4]
escolhido = random.choice(lista) # esse comando choice é usado para escolher dentro da variavel em ()
print(f'O aluno escolhido foi {escolhido}')
