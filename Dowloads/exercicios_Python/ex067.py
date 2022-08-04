while True:
    print('='* 30)
    n = int(input('\33[30mQuer ver a tabuada de qual valor?: '))
    print('=' * 30)
    c = 0
    while c < 10:
        c += 1
        print(f'\33[33m{n} x {c:2} = {n * c}')
    if n <= 0:
        break
print('='* 30)
print('\33[37mPROGRAMA TABUADA ENCERRADO! Volte sempre')
