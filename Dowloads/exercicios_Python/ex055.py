cont = maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Qual é o peso da {c}ª pessoa: '))
    if cont == 0:
        cont += 1
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior:.1f}\nO menor peso lido foi {menor:.1f}')