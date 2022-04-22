lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado! Digite outro valor...')
    else:
        lista.append(valor)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont in 'N':
        break
print('-=' * 20)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 NÃO faz parte da lista.')
