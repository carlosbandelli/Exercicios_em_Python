divida = int(input())
pagar = int(input())
counter = 1

while divida > 0:
  print(f'pagamento: {counter}')
  print(f'antes = {divida}')

  if divida < pagar:
    divida = 0
  else:
    divida -= pagar

  print(f'depois = {divida}')
  print('-'*5)
  counter += 1










