print('-' * 30)
print(' LOJA SUPER BARATÃO '.center(30))
print('-' * 30)
total = caro = barato = 0
maisbarato = ''
while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    total += preco
    if preco > 1000:
        caro += 1
    if barato == 0:
        barato = preco
        maisbarato = nome
    elif preco < barato:
        barato = preco
        maisbarato = nome
    if cont in 'N':
        break
print('FIM DO PROGRAMA')
print(f'O Total da compra foi R$ {total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {maisbarato} qua custa R$ {barato:.2f}')
