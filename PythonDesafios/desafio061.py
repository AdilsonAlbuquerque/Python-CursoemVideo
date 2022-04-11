p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 10
while cont >= 1:
    print(p, end=' ')
    p = p + r
    cont -= 1
