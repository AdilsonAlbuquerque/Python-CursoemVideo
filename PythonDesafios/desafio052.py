n = int(input('Digite um número intero: '))
if n == 1:
    print('O número {} não é primo'.format(n))
elif n > 2 and n % 2 == 0:
    print('O número {} não é primo'.format(n))
elif n > 3 and n % 3 == 0:
    print('O número {} não é primo'.format(n))
elif n > 5 and n % 5 == 0:
    print('O número {} não é primo'.format(n))
elif n > 7 and n % 7 == 0:
    print('O número {} não é primo'.format(n))
else:
    print('O número {} é primo'.format(n))
