l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print('Os segmentos podem formar um triângulo ',end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Não é um triângulo.')