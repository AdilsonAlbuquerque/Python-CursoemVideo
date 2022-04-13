import random
n1 = random.randint(0, 5)
n2 = int(input('Tente advinhar o número de 0 a 5: '))
if n1 == n2:
    print('Parabéns! Você acertou!\nO numero sorteado foi {}'.format(n1))
else:
    print('Que pena! Você errou!\nO número sorteado foi {}'.format(n1))
