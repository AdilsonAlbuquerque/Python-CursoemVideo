n = 0
soma = 0
cont = 0
while n < 999:
    n = int(input('Digite um número ou 999 para terminar: '))
    if n != 999:
        soma += n
        cont += 1
print('Foram digitados {} números e a soma entre eles é {}.'.format(cont, soma))
