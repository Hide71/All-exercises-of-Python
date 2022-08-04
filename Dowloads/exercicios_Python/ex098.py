from time import sleep
def contador(com, meio, fim):
    if fim < 0:
        fim *= -1
        if fim == 0:
            fim = 1
    print('-=' * 20)
    print(f'Contagem de {com} até {meio} de {fim} em {fim}')
    sleep(2)
    if com <= meio:
        c = com
        while c <= meio:
            print(f'{c} ', end=' ')
            c += fim
            sleep(.5)
        print('FIM!')
    else:
        c = com
        while c >= meio:
            print(f'{c}', end=' ')
            c -= fim
            sleep(.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('inicio:'))
me = int(input('meio:'))
fi = int(input('fim: '))
contador(ini, me, fi)




