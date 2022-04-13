print('Analizador de Triângulos')
r1 = float(input('Digite quantos cm tem a primeira reta: '))
r2 = float(input('Digite quantos cm tem a segunda reta: '))
r3 = float(input('Digite quantos cm tem a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3:
        print('Esse é um triangulo Equilátero!')
    if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Esse é um triangulo Isósceles!')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('Esse é um triangulo Escaleno!')
else:
    print('Essas retas não podem formar um triângulo!')
