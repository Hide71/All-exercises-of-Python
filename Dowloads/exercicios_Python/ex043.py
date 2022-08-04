peso = float(input('qual é o seu peso:(KG) '))
altura = float(input('Qual é sua altura: (M) '))
imc = peso / (altura ** 2)
print(f'Seu imc é: {imc:.1f}')
if imc <= 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')