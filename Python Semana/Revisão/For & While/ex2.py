valortotal = 0
while True:
    print('Doritos 1- 10R$')
    print('Cheetos 2- 8R$')
    print('Baconzitos 3- 9R$')
    print('Cebolitos 4- 7R$')
    quer = input('Deseja comprar algo? [S/N]: ').upper()
    if quer == 'N':
        break
    comprar = int(input('Deseja comprar o que?: '))
    if comprar == 1:
         valortotal += 10
    elif comprar == 2:
        valortotal += 8
    elif comprar == 3:
        valortotal += 9
    elif comprar == 4:
        valortotal += 7
print(valortotal)