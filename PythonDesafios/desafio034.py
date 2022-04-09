sal = float(input('Qual o salário atual? R$ '))
if sal > 1250.00:
    aum = sal + (sal * 0.10)
    print('Seu salário é R$ {:.2f}'.format(sal))
    print('Com aumento de 10% vai passar a ser R$ {:.2f}'.format(aum))
else:
    aum = sal + (sal * 0.15)
    print('Seu salário é R$ {:.2f}'.format(sal))
    print('Com aumento de 15% vai passar a ser R$ {:.2f}'.format(aum))
