from random import randint
c = 0
while True:
    comp = randint(0, 10)
    print('='*30)
    print('Vamos jogar Par ou Impar')
    print('='*30)
    jog = int(input('Diga um valor: '))
    resp = str(input("Par ou Ìmpar?: "))
    total = comp + jog
    if resp in "Pp":
        if total % 2 == 0:
            print('=' * 30)
            print(f'você jogou {jog} e o computador jogou {comp}, total: {total}. Deu PAR')
            print('=' * 30)
            print('Você venceu Vamos jogar novamente...')
            c += 1
        else:
            print('=' * 30)
            print(f'você jogou {jog} e o computador jogou {comp}, total: {total}. Deu IMPAR')
            print('=' * 30)
            print('Voce Perdeu!!')
            break
    if resp in "Ii":
        if total % 2 != 0:
            print('=' * 30)
            print(f'você jogou {jog} e o computador jogou {comp}, total: {total}. Deu IMPAR')
            print('=' * 30)
            print('Você venceu Vamos jogar novamente...')
            c += 1

        else:
            print('=' * 30)
            print(f'você jogou {jog} e o computador jogou {comp}, total: {total}. Deu PAR')
            print('=' * 30)
            print('Voce Perdeu!!')
            break
print(f'Game over voce venceu {c} vezes')

