contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco'
            , 'seis', 'sete', 'oito', 'nove', 'dez', 'onze'
            , 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis'
            , 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))

while True:
    if numero in range(0, len(contagem)):
        print(f'Você digitou o número {contagem[numero]}')
        break
    else:
        print('Tente novamente.', end=' ')
        numero = int(input('Digite um número entre 0 e 20: '))


