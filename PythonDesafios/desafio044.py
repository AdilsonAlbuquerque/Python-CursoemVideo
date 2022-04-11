valor = float(input('Digite o preço: R$ '))
cond = int(input('Condições de pagamento:\n'
                 '0 - À vista Dinheiro/Cheque com 10% de desconto;\n'
                 '1 - À vista no Cartão com 5% de desconto;\n'
                 '2 - Até 2x no Cartão (preço normal);\n'
                 '3 - 3x ou mais no Cartão com 20% de juros.\n'
                 'Digite o número da forma de pagamento: '))
if cond == 0:
    valor = valor - (valor * 10 / 100)
    print('O valor da compra será R${:.2f}'.format(valor))
elif cond == 1:
    valor = valor - (valor * 5 / 100)
    print('O valor da compra será R${:.2f}'.format(valor))
elif cond == 2:
    print('O valor da compra será R${:.2f}'.format(valor))
elif cond == 3:
    valor = valor + (valor * 20 / 100)
    print('O valor da compra será R${:.2f}'.format(valor))
else:
    print('Opção inválida!')
