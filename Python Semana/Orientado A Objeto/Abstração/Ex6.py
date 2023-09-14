class lampada():
    def __init__(self,status):
        self.status = status
    def ligar(self):
        self.status = 'Ligado'
    def Desligar(self):
        self.status = 'Desligado'
    def exibir(self):
        print(self.status)
lampada1 = lampada('Desligado')
lampada1.ligar()
lampada1.exibir()
lampada1.Desligar()
lampada1.exibir()
