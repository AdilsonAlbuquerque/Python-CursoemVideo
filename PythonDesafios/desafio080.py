lista = []
for n in range(0, 5):
    valor = int(input('digite um número: '))
    if n == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicinado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 20)
print(f'Os valores adicionados em ordem foram: {lista}')
