s = 0
cont = 0
for i in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('Números pares informados: {} \nSoma dos número pares: {}'.format(cont, s))