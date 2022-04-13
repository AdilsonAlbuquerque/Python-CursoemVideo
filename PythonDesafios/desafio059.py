n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    soma = n1 + n2
    multi = n1 * n2
    opcao = int(input('''Opções:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    Escolha uma opção: '''))
    if opcao == 1:
        print('\nVocê escolheu SOMAR.')
        print('A soma entre {} e {} vale {}.\n'.format(n1, n2, soma))
    if opcao == 2:
        print('\nVocê escolheu MULTIPLICAR.')
        print('A multiplicação entre {} e {} vale {}.\n'.format(n1, n2, multi))
    if opcao == 3:
        print('\nVocê quer saber qual o MAIOR valor.')
        print('O maior valor entre {} e {} é {}.\n'.format(n1, n2, max(n1, n2)))
    if opcao == 4:
        print('\nVocê escolheu NOVOS NÚMEROS')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
print('>>> Fim <<<')
