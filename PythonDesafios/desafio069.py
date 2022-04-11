maioridade = homen = mulher = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('-' * 30)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homen += 1
    elif idade < 20:
        mulher += 1
    if cont in 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homen} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
