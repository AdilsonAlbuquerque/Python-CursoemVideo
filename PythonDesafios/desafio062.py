p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 11
while cont != 0:
    if cont != 1:
        print(p, end=' ')
        p = p + r
        cont -= 1
    else:
        cont = int(input('\nQuer mostrar mais quantos termos? '))
        if cont != 0:
            cont += 1
print('Fim')
