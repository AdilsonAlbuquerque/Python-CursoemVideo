sexo = ''
escolha = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida. Digite novamente!')
    elif sexo == 'M':
        escolha = 'Masculino'
    elif sexo == 'F':
        escolha = 'Feminino'
print('Você escolheu sexo {}'.format(escolha))
