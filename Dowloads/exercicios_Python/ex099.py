from time import sleep
def maior(* num):
    print('Analisando os valores passados...')
    c = maior =  0
    for v in num:
        print(f'{v}', end=' ')
        sleep(1)
        if c == 0:
            maior = v
        if v > maior:
            maior = v
        c += 1
    print(f'Foram informados {c} valores ao todo.')
    print(f'O maior valor informao foi {maior}')
    print('-=' * 20)



maior(3, 5, 7)
maior(3, 9, 2, 6, 0)
maior(6, 9)
maior()



