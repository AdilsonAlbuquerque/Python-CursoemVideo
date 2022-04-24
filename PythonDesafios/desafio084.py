lista = list()
dado = list()
pesado = list()
leve = list()
maior = list()
menor = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
for p in lista:
    if p[1] >= 100:
        pesado.append(p[0])
        maior.append(p[1])
    elif p[1] <= 70:
        leve.append(p[0])
        menor.append(p[1])
print('-=' * 25)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'Os maiores pesos foram de {maior}Kg. Peso de {pesado}')
print(f'Os menores pesos foram de {menor}Kg. Peso de {leve}')
