valor = float(input('valor do item: '))
qtd = int(input('Quantidade:'))
total = valor*qtd
desconto= total * (0.10+(qtd *0.01))
total_final = total - desconto
print(f'Total sem desconto:R${total:.2f}')
print(f'Total com desconto:R${total_final:.2f}')
