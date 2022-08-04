jog = {}
gols = []
listagem = []
while True:
    jog['nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {jog["nome"]} jogou?:  '))
    for c in range(0, part):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jog['gols'] = gols.copy()
    jog['total'] = sum(jog['gols'])
    gols.clear()
    listagem.append(jog.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Somente S ou N')
    if resp == 'N':
         break
print('-='*30)
print('cod', end='')
for i in jog.keys():
    print(f'{i:>15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(listagem):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-='*30)
while True:
    esc = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if esc == 999:
        break
    if esc >= len(listagem):
        print(f'Erro não existe jogador com codigo {esc} ')
    else:
        print(f'Levantamento do jogador {listagem[esc]["nome"]}')
        for i, v in enumerate(listagem[esc]["gols"]):
            print(f'No jogo {i} fez {v} gols ')
