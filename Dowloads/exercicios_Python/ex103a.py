def ficha(a=('<desconhecido>'), b=0):
     print(f'O jogador {a} fez {b} gols no campeonato.')




n = str(input('Nome do jogador: '))
gol = str(input('Quantos gols'))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if n.strip() == '':
    ficha(b=gol)
else:
    ficha(n, gol)