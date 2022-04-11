from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    if date.today().year - nasc >= 21:
        maior += 1
    elif date.today().year - nasc < 21:
        menor += 1
print('{} pessoas ainda não atingiram a maioridade'.format(menor))
print('{} pessoas já são maiores'.format(maior))
