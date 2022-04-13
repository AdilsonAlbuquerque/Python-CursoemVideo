from random import randint
print('Vamos Jogar Jokenpô!!!')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Escolha uma opção:\n'
                    '0 - PEDRA; 1 - PAPEL; OU 2 - TESOURA\n'
                    'Digite aqui: '))
pc = randint(0, 2)
if jogador < 0 or jogador > 2:
    print('Jogada inválida! Tente Novamente!')
    quit()
print('O computador escolheu: {}'.format(lista[pc]))
print('O jogador escolheu: {}'.format(lista[jogador]))
if pc == 0:
    if jogador == 0:
        print('>>>EMPATOU<<<')
    elif jogador == 1:
        print('>>>VOCÊ GANHOU<<<')
    elif jogador == 2:
        print('>>>VOCÊ PERDEU<<<')
elif pc == 1:
    if jogador == 1:
        print('>>>EMPATOU<<<')
    elif jogador == 2:
        print('>>>VOCÊ GANHOU<<<')
    elif jogador == 0:
        print('>>>VOCÊ PERDEU<<<')
elif pc == 2:
    if jogador == 2:
        print('>>>EMPATOU<<<')
    elif jogador == 0:
        print('>>>VOCÊ GANHOU<<<')
    elif jogador == 1:
        print('>>>VOCÊ PERDEU<<<')
