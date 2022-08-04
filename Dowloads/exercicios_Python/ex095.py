jogs = {}
gols = []
lista =[]
while True:
    total = 0
    jogs['nome'] = str(input('nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogs["nome"]} jogou?: '))
    for c in range(0, quant):
        g = (int(input(f'Quantos gols na partida {c + 1}?:')))
        total += g
        gols.append(g)
    jogs['gol'] = gols[:]
    gols.clear()
    jogs['tot'] = total
    lista.append(jogs.copy())
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print('  cod', end='')
for i in jogs.keys():
    print(f'{i:>15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(lista):
    print(f'{k:>4} ', end='')
    for n in v.values():
        print(f'{str(n):>15}', end='')
    print()
while True:
    d = int(input('Quer mostrar dados de qual jogador?(999 para parar): '))
    if d == 999:
        break
    if d >= len(lista):
        print(f'valor {d} não existe ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[d]["nome"]}: ')
        for i, g in enumerate(lista[d]['gol']):
            print(f'     no jogo{i + 1}, fez {g} gols.')