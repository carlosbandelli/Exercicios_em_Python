dia_compra = input()
prazo = int(input())


if dia_compra == 'domingo':
    dia_numero = 0
elif dia_compra == 'segunda':
    dia_numero = 1
elif dia_compra == 'terca':
    dia_numero = 2
elif dia_compra == 'quarta':
    dia_numero = 3
elif dia_compra == 'quinta':
    dia_numero = 4
elif dia_compra == 'sexta':
    dia_numero = 5
elif dia_compra == 'sabado':
    dia_numero = 6

dia_entrega = dia_numero + prazo
if dia_entrega > 6:
    dia_entrega = dia_entrega -7

if prazo == 0:
    print('chega hoje!')
elif dia_entrega == 0:
    print('sera entregue domingo')
elif dia_entrega == 1:
    print('sera entregue segunda')
elif dia_entrega == 2:
    print('sera entregue treca')
elif dia_entrega == 3:
    print('sera entregue quarta')
elif dia_entrega == 4:
    print('sera entregue quinta')
elif dia_entrega == 5:
    print('sera entregue sexta')
elif dia_entrega == 6:
    print('sera entregue sabado')
    
