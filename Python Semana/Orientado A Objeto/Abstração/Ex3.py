class conta():
    def __init__(self,titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
    def deposito(self):
        valor = int(input('Diga o valor pra ser depositado: '))
        self.saldo = self.saldo+valor
    def saque(self):
        while True:
            valor = int(input('Diga o valor pra ser sacado: '))
            if valor > self.saldo:
                print('Saque maior que seu saldo!, tente sacar menos')
            else:
                self.saldo = self.saldo - valor
                break
    def exibir(self):
        print(f'Seu saldo é {self.saldo}')
Henri = conta('Henri', 1000,90)
Henri.saque()
Henri.deposito()
Henri.exibir()