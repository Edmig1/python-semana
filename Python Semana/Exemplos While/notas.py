total= 0
vezes = 0
while True:
    nota = float(input('Digite a Nota: '))
    if(nota<0):
        break
    total += nota

    vezes += 1
print(total/vezes)