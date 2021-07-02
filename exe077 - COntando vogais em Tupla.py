palavras = ('aprender', 'programar', 'Linguagem', 'python',
            'cruso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras: # para cada palavra dentro do array de palavra
    print(f'\nNa palavra {p.upper()} temos', end='')
    for letra in p: # para cada letra de palvra tirado do array palavras
        if letra.lower() in 'aeiou':
            print(letra, end=' ')