# Importando randint
from random import randint
# Declarando a variável valores que vai receber os números do randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# Mostrando os valores sorteados
print(f'Os valores sorteados foram: {valores}')
# Mostrando o maior valor sorteado
print(f'O maior valor sorteado foi {max(valores)}')
# Mostrando o menor valor sorteado
print(f'O menor valor sorteado foi {min(valores)}')
