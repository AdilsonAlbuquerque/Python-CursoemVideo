d = float(input('Qual a distância da viagem em km? '))
if d <= 200:
    v = d * 0.50
    print('Sua viagem será de {} km'.format(d))
    print('Sua passagem custará R$ {:.2f}'.format(v))
else:
    v = d * 0.45
    print('Sua viagem será de {} km'.format(d))
    print('Sua passagem custará R$ {:.2f}'.format(v))
