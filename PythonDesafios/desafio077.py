palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for vogal in c:
        if vogal in 'aeiou':
            print(vogal, end=' ')


