from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1

    print(f'contagem de {i} até {f} de {p} em {p}: ')
    print('~' * 30)
    sleep(2)
    if i <= f:
        c = i
        while c <= f:
            print(f'{c}', end=' ')
            sleep(.5)
            c += p
        print('FIM')
        print('-=' * 15)
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ')
            sleep(.5)
            c -= p
        print('FIM')
        print('-=' * 15)



contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

