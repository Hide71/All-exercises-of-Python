soma = cont = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f'Você digitou {cont} numeros pares, e a soma total foi {soma}')
