res = 's'
while res == 's':
    num = int(input('Digite um número: '))
    if num >= 999:
        print('número muito grande')
    res = str(input('Deseja coninuar: S/N '))