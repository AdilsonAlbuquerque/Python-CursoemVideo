expressao = str(input('Digite a expressão: '))
abre = []
fecha = []
for parentese in expressao:
    if parentese == '(':
        abre.append('(')
    elif parentese == ')':
        fecha.append(')')
        break
if len(abre) == len(fecha):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
