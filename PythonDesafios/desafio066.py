soma = total = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    soma += n
    total += 1
print(f'Foram digitados {total} números e a soma entre eles foi {soma}')
