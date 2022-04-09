r1 = float(input('Digite quantos cm tem a primeira reta: '))
r2 = float(input('Digite quantos cm tem a segunda reta: '))
r3 = float(input('Digite quantos cm tem a terceira reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Sim, essas retas podem formar um triangulo!')
else:
    print('Não, essas retas não podem formar um triangulo!')
