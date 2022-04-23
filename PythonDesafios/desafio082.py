lista = []
while True:
    lista.append(int(input(f'Digite um número: ')))
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont in 'N':
        break
print(f'A lista completa é {lista}')
par = []
impar = []
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
