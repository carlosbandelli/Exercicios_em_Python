import math
ângulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(ângulo))# ele vai pegar o valor de angulo transformar em radianos e depois faz consseno
print(f'O ângulo de {ângulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(ângulo))
print(f'O angulo de {ângulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print(f'O angulo de {ângulo} tem a tangente de {tangente:.2f}')