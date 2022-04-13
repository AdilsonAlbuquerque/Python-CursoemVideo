from random import randint
computador = randint(0, 10)
print('-=-' * 17)
print('Vou pensar em um número de 0 a 10. Tente advinhar')
print('-=-' * 17)
jogador = 11
cont = 0
while computador != jogador:
    jogada = int(input('Em que número eu pensei? '))
    jogador = jogada
    cont += 1
    if computador > jogador:
        print('Mais... Tente outra vez.')
    elif computador < jogador:
        print('Menos... Tente outra vez.')
print('\nParavéns! Você acertou na {}ª tentativa.'.format(cont))
