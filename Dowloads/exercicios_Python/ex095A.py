dic = {}
gols = []
lista = []
while True:
    dic['nome'] = (str(input('Nome do jogador: ')))
    part = int(input(f'Quantas partidas {dic["nome"]} jogou?: '))
    for c in range(0, part):
       gols.append(int(input(f'Quantos gols na partida {c}: ')))
    dic['gols'] = gols[:]
    gols.clear()
    dic['total'] = sum(dic["gols"])
    lista.append(dic.copy())
    while True:
        resp = str(input('Quer continuar?[S/|N]: ')).upper()[0]
        if resp in 'SsNn':
            break
        print('Erro digite somente S ou N ')
    if resp == 'N':
        break

print('-=' * 30)
print(f'  {"cod"}', end=' ')
for c in dic.keys():
    print(f'{c:>15}', end='')
print()
print('-=' * 30)
for i, v in enumerate(lista):
    print(f'{i:>4}', end='')
    for n in v.values():
        print(f'{str(n):>15}', end='')
    print()
while True:
    jog = int(input('Mostrar dado de qual jogador?(999 para parar): '))
    if jog == 999:
        break
    if jog >= len(lista):
        print('erro digite novamente')
        print(f'LEVANTAMENTO DO JOGADOR {lista[jog]["nome"]}')
    else:
        for i, v in enumerate(lista[jog]['gols']):
            print(f'Na partida {i + 1} fez {v} gols')


º