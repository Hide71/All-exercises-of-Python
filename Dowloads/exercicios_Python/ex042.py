l1 = float(input('Lado1: '))
l2 = float(input('Lado2: '))
l3 = float(input('Lado3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\33[36mOs lados podem formar um triangulo:', end=' ')
    if  l1 == l2 and l2 == l3:
        print('\33[33mEQUÍLATERO')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('\33[33mISOSCELES')
    elif l1 != l2 != l3:
        print('\33[33mESCALENO')
else:
    print('\33[36mOs lados não formam triangulo')

