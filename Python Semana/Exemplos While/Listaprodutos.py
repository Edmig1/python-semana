print('Doritos-10R$')
print('Ruffles-12R$')
print('Fandangos-9R$')
print('Cebolitos-7R$')
def compras():
    total = 0
    maiscaro = 0
    nomecaro = ''
    while True:
        escolha = str(input('Qual salgadinho você deseja: '))
        if(escolha == 'Doritos'):
            total += 10
            if(maiscaro < 10):
                maiscaro = 10
                nomecaro = 'Doritos'
        elif(escolha == 'Ruffles'):
            total += 12
            if (maiscaro < 12):
                maiscaro = 12
                nomecaro = 'Ruffles'
        elif(escolha == 'Fandangos'):
            total += 9
            if (maiscaro < 9):
                maiscaro = 9
                nomecaro = 'Fandangos'
        elif(escolha == 'Cebolitos'):
            total += 7
            if (maiscaro < 7):
                maiscaro = 7
                nomecaro = 'Cebolitos'
        sair = str(input('Deseja sair? responda com S/N: '))
        if(sair == 'S'):
            break
    print(total)
    print(nomecaro)
compras()