a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços ? ', a.isspace())# esse comando mostra que tem espaços
print('È numero ?', a.isnumeric())# esse comando mostra que tem numero
print('È alphabetico ?', a.isalpha())# esse comando mostra se é alphabetico
print('È alfanumerico ?', a.isalnum())# esse comando mostra se alpha numeric
print('Está em maiusculas', a.isupper())# esse comando mostra se é maiuscula
print('Está em minuscula ?', a.islower())# esse comanod mostra se ta em minuscula
print('Èstá capitalizada ?', a.istitle())# esse metodo mostra se ta com estilo