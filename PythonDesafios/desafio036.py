casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Dividir em quantos anos? '))
meses = anos * 12
parcela = casa / meses
if parcela <= (salario * 30 / 100):
    print('Concedido! A parcela ficará no valor de R${:.2f} mensais'.format(parcela))
else:
    print('Negado! O valor da parcela R${:.2f} ultrapassa o limite de 30% do seu salário.'.format(parcela))
