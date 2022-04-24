lista = []
par = []
impar = []
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
lista.append(par)
lista.append(impar)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores pares digitados foram: {lista[1]}')
