frase = 'Curso em video python'
print(frase) # desse modo mostra a frase
print(frase[3]) # monstra a letra que voce quer denteo do array lembrando que semore se começa a contagem do numero 0, ness casa vai mostra a 4ª letra
print(frase[3:13])# começa da quarta letra e vai ate a letar 12 se quiser ir ate a letra 13 acresente +1 ele sempre conta um a menos
print(frase[:13])# quando nao se coloca nenhum numero antes do  ':' ele considera isso do inicio
print(frase[1:15:2])# quando se coloca esses parametros o 1º significa onde começa, 2º até onde vai, 3º passos, nesse caso 2 em 2
print(frase[::2])#vai do inicio ate o final da string pulando dois e dois
#para colocar um texto inteiro dentro do print acrescente tres vezes ''' exemplo abaixo
print(""" kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkk""")
print(frase.count('o'))# para contar quantas letras tem em uma string voce usa o metodo count e ele te da quantas letras tem no stirng.
print(frase.count('o',0,13)) # esse modo mostra 1º oque vai contrar, 2º da onde vai começar, 3º da onda vai terminar
print(frase.capitalize())# esse metodo vai colocar tudo em minuscula e só a primeira letra do inicio vai virar maiuscula
print(frase.title()) # esse metodo vai analizar a frase pelo espaços e assim no final e no começo da cada espaço as letro que suceder o espaço recebe uma letra maiuscula
print(frase.upper())# esse metrodo serve para deixar todas as letras da string em maiusculas
print(frase.upper().count('O')) # assim voce deixa a frase toda em maiusculas e ainda procura a letra maiuscula
print(len(frase)) # esse metodo é para sabe o tamanho da frase "length"
print(len(frase.strip())) # esse stripe serve para remover os espaço inutis no inicio e no final da string da string
print(frase.rstrip()) # esse metodod remove os espaços inuteis só da direita
print(frase.lstrip()) # esse metodos remove os espaços inuteis só da esquerda
print(frase.replace('python', 'Android')) #esse metodo serve para troca uma sring para outra.1º se coloca o que voce quer troca, 2º pelo que voce vai trocar
#esse metodo replace serve para mudar na instacia, porem nao serve parar deixar salvo
# para deixar salvo precisa frase assim
frase = frase.replace('Python','Android')
# esse modo ele salva na memoria
print(frase)
# para saber se uma palavra esta dentro da frase usasse, o seguinte comando que a resposta vai ser boolean
print('Curso' in frase)
print(frase.find('Video'))#quando usa esse comando monstra a posição do que inicia a frase.
print(frase.split()) #esse metodo separa palavra por palavra transformando em um array.
dividido = frase.split()
print(dividido[0])#esse modo mostra aplavra que esta na posição 0
print(dividido [2] [3]) #esse modo voce fala assim pro print: pega a chave dois que é a plavra Vídeo e nela quero que voce mostre a letra na posição 3 (lemtra sempre com ta a partir do 0)
print(dividido.insert(1, 'a'))
print(''.join(frase))# voce adiciona espaça em uma string splitada




