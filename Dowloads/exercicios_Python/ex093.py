jogador = {}
lista = []
c = soma = 0
jogador['nome'] = str(input('Nome: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
while c < part:
     c += 1
     n =(int(input(f'Quantos gols na partida {c}?: ')))
     soma += n
     lista.append(n)
jogador['gol'] = lista
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for c, v in jogador.items():
     print(f'O campo {c} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]}, jogou {part} partidas. ')
for i, v in enumerate(lista):
       print(f'  => Na partida {i + 1},fez { v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')



