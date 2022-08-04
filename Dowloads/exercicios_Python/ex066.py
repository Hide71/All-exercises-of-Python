c = soma = 0
while True:
    n = int(input('Digite um numero[999 para parar]: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Você digitou {c} números, a soma de {soma}')