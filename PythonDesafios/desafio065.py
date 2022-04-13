n = 0
soma = 0
total = 0
cont = 0
maior = 0
menor = 0
while cont >= 0:
    n = int(input('Digite um número: '))
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    soma += n
    total += 1
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if escolha == 'S':
        cont += 1
    else:
        cont = -1
print('A média dos valores digitados é {:.1f}.'.format(soma/total))
if maior == menor:
    print('Todos os valores digitados foram iguais.')
else:
    print('O maior valor digitado foi {}.'.format(maior))
    print('O menor valor digitado foi {}.'.format(menor))
