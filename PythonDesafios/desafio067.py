while True:
    n = int(input('Quer ver a tabauada de qual valor? '))
    print('-=-' * 13)
    if n < 0:
        break
    c = 1
    while c <= 10:
        print(f'{n} x {c:2} = {n*c}')
        c += 1
    print('-=-' * 13)
print('Programa TABUADA Encerrado. Volte sempre!')
