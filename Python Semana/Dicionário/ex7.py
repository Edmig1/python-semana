from random import randint
d = {}
while True:
    nota = str(input('Digite Nome do jogador: '))
    d[nota] = randint(1,6)
    cont = str(input('Deseja Continuar? [S/N]'))
    if cont in 'Nn':
        print(d)
        break