from Pacotes.OpMat import multiplicacao,soma,divisao,subtracao
esc = int(input('Qual operação deseja?: \n1-Subtração\n2-Adição\n3-Multiplicação\n4-Divisão\n'))
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
if esc == 1:
    resultado = soma(n1,n2)
elif esc == 2:
    resultado = subtracao(n1,n2)
elif esc == 3:
    resultado = multiplicacao(n1,n2)
else:
    resultado = divisao(n1,n2)
print(resultado)