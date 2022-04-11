s = 0
n = 0
for c in range(3, 501, 3):
    if c % 3 == 0:
        if c % 2 != 0:
            s += c
            n += 1
print('A soma dos {} números ímpares multiplos de 3 é {}'.format(n, s))
