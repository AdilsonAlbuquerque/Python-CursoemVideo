lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 20)
print(f'Voce digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}... ', end='')
