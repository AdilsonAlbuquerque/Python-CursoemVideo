soma = 0
velho = 0
mulher = 0
homem = str()
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper()
    soma += idade
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    else:
        if sexo == 'M':
            velho = idade
        if idade > velho:
            homem = nome

print('Media das idades: {}'.format(soma/4))
print('Homem mais velho: {}'.format(homem))
print('Mulher menos de vinte: {}'.format(mulher))
