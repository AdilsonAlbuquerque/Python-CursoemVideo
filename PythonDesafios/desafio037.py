num = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha uma das opções para conversão:\n'
                    '- Digite 1 para binário;\n'
                    '- Digite 2 para octal;\n'
                    '- Digite 3 para hexadecimal;\n'
                    'Digite para conversão: '))
if escolha == 1:
    print('O número {} convertido para Binário é {}'.format(num, bin(num)))
elif escolha == 2:
    print('O número {} convertido para Octal é {}'.format(num, oct(num)))
elif escolha == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)))
else:
    print('A opção {} é inválido para conversão!'.format(escolha))
