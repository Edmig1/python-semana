num = []
while True:
    esc = int(input('Adicione um número'))
    if esc in num:
        num.pop()
    num.append(esc)
    sair = str(input('quer sair?'))
    if sair == 's':
        break
print (num)