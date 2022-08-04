dist = float(input('Qual é a distancia da sua viagem?: '))
print(f'Voce esta prestes a começar uma viagem de {dist}KM.')
if dist <= 200:
    preço = dist * .50
    print(f'E o preço de sua passagem será:R$ {preço:.2f}')
else:
    preço = dist * .45
    print(f'E o preço de sua passagem será:R$ {preço:.2f}')