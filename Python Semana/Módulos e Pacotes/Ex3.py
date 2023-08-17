from random import randint
aleatorio = randint(1,100)
contagem = 0
while True:
    chute = int(input('Chute um Número: '))
    if chute > aleatorio:
        print('O número é menor')
        contagem += 1
    elif chute <aleatorio:
        print('O número é maior')
        contagem += 1
    elif chute == aleatorio:
        print(f'Parabéns, você acertou, o numero era {chute}')
        print(f'Você acertou em {contagem+1} tentativas')
        break