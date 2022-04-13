from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
cat = atual - ano
if cat <= 9:
    print('MIRIM')
elif cat > 9 and cat <= 14:
    print('INFANTIL')
elif cat > 14 and cat <=19:
    print('JUNIOR')
elif cat > 19 and cat <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
