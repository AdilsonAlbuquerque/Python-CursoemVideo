print('=' * 30)
print('BANCO CEV'.center(30))
print('=' * 30)
cinquenta = vinte = dez = um = 0
while True:
    valor = int(input('Qual valor você quer sacar? '))
    if valor // 50 > 0:
        cinquenta = valor // 50
        valor = valor - (50 * cinquenta)
        print(f'Total de {cinquenta} cédulas de R$50')
    if valor // 20 > 0:
        vinte = valor // 20
        valor = valor - (20 * vinte)
        print(f'Total de {vinte} cédulas de R$20')
    if valor // 10 > 0:
        dez = valor // 10
        valor = valor - (10 * dez)
        print(f'Total de {dez} cédulas de R$10')
    if valor // 1 > 0:
        um = valor // 1
        valor = valor - (1 * um)
        print(f'Total de {um} cedulas de R$1')
    if valor == 0:
        break
print('Volte sempre ao BANCO CEV! tenha um bom dia!')
