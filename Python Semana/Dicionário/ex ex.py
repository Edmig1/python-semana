df = {}
while True:
    ele = str(input('Digite um elemento: '))
    df[ele] = str(input(f'Digite um valor do elemento {ele}: '))
    cont = str(input('Deseja Continuar? [S/N]'))
    if cont in 'Nn':
        break
print(df)