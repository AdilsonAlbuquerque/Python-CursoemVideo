p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(p, p+r*10, r):
    print(c, end=' ')
