nome = input ('Qual é seu nome ?')
print('Print em te conhecer {:20}!'.format(nome)) #escreveu o nome em :20 espaços
print('Print em te conhecer {:>20}!'.format(nome)) #escreveu o nome em :20 espaços e usando > fica alinhado á direita
print('Print em te conhecer {:<20}!'.format(nome))  #escreveu o nome em :20 espaços e usando < fica alinhado á esquerda
print('Print em te conhecer {:^20}!'.format(nome))  #escreveu o nome em :20 espaços e usando ^ fica centralizado
print('Print em te conhecer {:=^20}!'.format(nome))  #escreveu o nome em :20 espaços e usando ^ fica centralizado e coloca o caracter e ainda o nome no meio do caracter
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s},\n o produto é {m},\n ea divisão é {d:.3f}', end =' , ')# essa \n significa quebra de linha dentro do print e o :.3f signifca quantas casa apos a virgula eu quero
print (f'Divisão inteira {di} e Potencia {e}')# end='' signifca que o print que viar a seguir vai continuar na mesma linha