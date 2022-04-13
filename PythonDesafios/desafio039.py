from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
prazo = atual - ano
if prazo < 18:
    falta = 18 - prazo
    print('Falta(m) {} ano(s)'.format(falta))
elif prazo == 18:
    print('Está na hora')
elif prazo > 18:
    passou = prazo - 18
    print('Passou(se) {} ano(s)'.format(passou))
