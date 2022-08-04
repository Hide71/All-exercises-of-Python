from time import sleep
n1 = int(input('\33[37mPrimeiro valor: '))
n2 = int(input('Segundo valor: \33[m'))
while True:
    print('''\33[36m[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa\33[m''')
    print('=' * 30)
    sleep(1)
    escolha = int(input('>>>> Qual é a sua opção?:'))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif escolha == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} e {n2} é {produto}')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é o maior número')
        else:
            print(f'{n2} é o maior numero')
    elif escolha == 4:
        n1 = int(input('primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        break
    else:
        escolha >= 6
        print('Erro!! Digite novamente!')

