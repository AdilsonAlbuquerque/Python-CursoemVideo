v = float(input('Digite a velocidade do carro em Km/h: '))
if v > 80:
    m = (v - 80) * 7
    print('A velocidade está acima de 80 km/h')
    print('Você foi multado!')
    print('A multa vai custar R$ {:.2f}'.format(m))
else:
    print()
