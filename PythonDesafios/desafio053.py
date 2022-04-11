frase = str(input('Digite uma frase: ')).strip().upper()
normal = frase.replace(' ','')
inverso = normal[::-1]
print('O inverso de {} é {}'.format(normal, inverso))
if normal == inverso:
    print('Essa frase é um Palíndromo')
else:
    print('Não é um Palíndromo')
