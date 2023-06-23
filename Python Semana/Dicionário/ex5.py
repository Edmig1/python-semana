d = {}
while True:
    nota = str(input('Digite Nome do aluno: '))
    d[nota] = int(input('Digite a Nota do Estúpido: '))
    cont = str(input('Deseja Continuar? [S/N]'))
    media = d.values()
    media = list(media)
    if cont in 'Nn':
        print(d)
        print(sum(media)/len(media))
        break