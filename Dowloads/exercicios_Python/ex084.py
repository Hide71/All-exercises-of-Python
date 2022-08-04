lista = []
lista2 = []
mai = men = cont = 0
nomep = nomel = ' '
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('peso: ')))
    if len(lista2) == 0:
        mai = men = lista[1]
    else:
        if lista[1] > mai:
            mai = lista[1]
        if lista[1] < men:
            men = lista[1]
    lista2.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar?:'))
    if resp in "Nn":
        break
print(f'Ao todo você cadstrou {len(lista2)} pessoas. ')
print(f"O maior peso foi {mai} , Eles são: ")
for p in lista2:
    if p[1] == mai:
        nomep = p[0]
        print(f'{nomep}', end=', ')
print(f'\nO menor peso foi {men}, Eles são:')
for p in lista2:
    if p[1] == men:
        men = p[1]
        nomel = p[0]
        print(f'{nomel}', end=', ')