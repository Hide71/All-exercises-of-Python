tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
    'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis',
    'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero de 0 a 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o nimero{tupla[n]}')
        break
    else:
         print('ERRO!')