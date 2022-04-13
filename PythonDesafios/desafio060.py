n = int(input("Fatorial de: ") )
fat = 1
cont = 1
'''while cont <= n:
    fat *= cont
    cont += 1
print('O fatorial de {} é igual a {}'.format(n, fat))'''

for cont in range(n, 0, -1):
    fat *= cont
    cont += 1
print('fat com for {}'.format(fat))
