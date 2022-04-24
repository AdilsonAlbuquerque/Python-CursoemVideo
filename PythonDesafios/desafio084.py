lista = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('-=' * 25)
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
