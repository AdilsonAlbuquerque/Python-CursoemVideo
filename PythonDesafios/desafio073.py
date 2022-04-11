tabela = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
          'Bragantino', 'Fluminense', 'América MG', 'Atlético GO', 'Santos',
          'Ceará', 'Internacional', 'São Paulo', 'Atlético PR', 'Cuiabá',
          'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print('-=' * 21)
print(f'Lista de classificação do Brasileirão 2021: {tabela}')
print('-=' * 21)
print(f'Os 5 primeiros foram {tabela[:5]}')
print('-=' * 21)
print(f'Os 4 últimos foram {tabela[-4:]}')
print('-=' * 21)
print(f'Times em ordem alfabéticas: {sorted(tabela)}')
print('-=' * 21)
pos = tabela.index('Chapecoense') + 1
print(f'A Chapecoense terminou na {pos}ª posição.')
