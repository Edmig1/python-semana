from Pacotes.OpMat import area_quadrado, area_circulo
esc = int(input('Digite 1 para quadrado e 2 para círculo: '))
if esc == 1:
    v1 = float(input('Valor do lado: '))
    print('Se for um quadrado, a área é: ')
    area_quadrado(v1)
else:
    v1 = float(input('Número 1: '))
    print('Se for um círculo, a área é: ')
    area_circulo(v1)