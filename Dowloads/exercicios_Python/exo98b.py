from time import sleep
def contador(a, b, d):
    print(f'Contagem de {a} a {b} de {d} em {d}: ')
    print('-=' * 30)
    while a <= b:
        if b < a:
            a -= d
        print(f'{a}', end=' ')
        a += d
        sleep(1)
    print('FIM')
    print('-='*30)


contador(1, 10, 1)
contador(10, 0, 2)