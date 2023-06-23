nome = ('Penne ao Molho Branco', 'Lasanha Bolonhesa', 'Pizza', 'Pastel', 'Burguer')
preco = (25, 19, 45, 12, 25)
valortotal = []
qtd = 0
def escolha ():
    print('Aqui temos nosso cardápio: ',nome)
    qtd = 0
    qtd +=1
    esc = int(input('Escolha o número de um prato: '))
    esc = esc-1
    valortotal.append(preco[esc])
    if qtd < 4:
        esc = int(input('Deseja pedir mais? 1-sim, 2-não: '))
        if(esc == 1):
            escolha()
        else:
            print(sum(valortotal))
    else:
        print(sum(valortotal))
escolha()