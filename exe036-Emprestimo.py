casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de fianciamento? '))
prestação = casa/ (anos * 12)
minimo = salário * 30/100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a pretação será de R${prestação}')
if prestação <= minimo:
    print(f'Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
