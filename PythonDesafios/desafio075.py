valores = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))
print(f'Os valores digitados foram {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')
par = 0
print('Os valores pares digitados foram ', end='')
for c in valores:
    if c % 2 == 0:
        print(f'{c} ', end='')
        par+= 1
if par == 0:
    print('0, ou seja, nenhum.')
