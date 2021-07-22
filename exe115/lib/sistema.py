from interface import cabeçalho
from interface import leiaInt
from interface import menu
from arquivo import arquivoExiste
from arquivo import criarArquivo
from arquivo import lerArquivo
from arquivo import cadastrar
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVOV CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou um aopção errada no menu
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)