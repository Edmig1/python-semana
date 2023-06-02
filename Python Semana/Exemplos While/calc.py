n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
while True:
    esc = str(input(('1-Adição \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n 5-Sair do Programa \n Faça Sua Operação: ')))
    if(esc == '1'):
        print(n1+n2)
    if(esc == '2'):
        print(n1-n2)
    if(esc == '3'):
        print(n1*n2)
    if(esc == '4'):
        print(n1/n2)
    if(esc == '5'):
        break
