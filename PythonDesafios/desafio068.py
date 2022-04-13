from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
tentativa = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print('--' * 15)
    soma = jogador + computador
    if escolha in 'P':
        if soma % 2 == 0:
            escolha = 'PAR'
            tentativa += 1
            print(f'Você jogou {jogador} e o computador {computador}.', end='')
            print(f' Total de {soma}, DEU {escolha}.')
            print('--' * 15)
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=-' * 15)
        else:
            escolha = 'ÍMPAR'
            break
    else:
        if soma % 2 == 1:
            escolha = 'ÍMPAR'
            tentativa += 1
            print(f'Você jogou {jogador} e o computador {computador}.', end='')
            print(f' Total de {soma}, DEU {escolha}.')
            print('--' * 15)
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=-' * 15)
        else:
            escolha = 'PAR'
            break
print(f'Você jogou {jogador} e o computador {computador}.', end='')
print(f' Total de {soma}, DEU {escolha}.')
print('--' * 15)
print('Você PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {tentativa} vezes.')
