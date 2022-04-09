s = float(input('Digite seu salário: R$ '))
#a = s * 15 / 100
#ns = s + a
ns = s + (s * 15 / 100)
print('Novo salário com 15% de aumento: R$ {:.2f}'.format(ns))
