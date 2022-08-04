def ajuda(a):
    help(a)






a = ''
while True:
    a = str(input('biblioteca ou função: '))
    if a == 'fim':
        break
    else:
        ajuda(a)