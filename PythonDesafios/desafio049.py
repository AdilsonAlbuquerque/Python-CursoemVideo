n = int(input('Digite um número inteiro: '))
print('_' * 20)
print('*** TABUADA DE {} ***'.format(n))
print('_' * 20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, c*n))
print('_' * 15)
