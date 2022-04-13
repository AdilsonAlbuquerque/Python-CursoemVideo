p = float(input('Digite o preço do produto: R$ '))
#d = p * 5 / 100
#np = p - d
np = p - (p * 5 / 100)
print('Novo preço com 5% de desconto: R$ {:.2f}'.format(np))
