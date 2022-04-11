n = int(input('Numero: '))
p = 1
s = 1
cont = -1
while cont <= n - 2:
    if cont < 0:
        print(0, end=' ')
        cont += 1
    elif cont < 2:
        print(1, end=' ')
        cont += 1
    else:
        t = p + s
        print(t, end=' ')
        p = s
        s = t
        cont += 1
print('\nEsses são os {} primeiros elementos da sequencia de Fibonacci'.format(n+2))
