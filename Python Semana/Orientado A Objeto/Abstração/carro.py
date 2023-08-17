class Carro():
    def __init__(self,nome,marca,ano,cor,numportas,maxvel,status):
       self.nome = nome
       self.marca = marca
       self.ano =ano
       self.cor = cor
       self.numportas = numportas
       self.maxvel = maxvel
       self.stauts = status
    def ligar (self):
        self.status = 'Ligado'
    def Desligar(self):
        self.status = 'Desligado'
    def Corres(self):
        print('Correndo')
CitroenC3 = Carro('CitroenC3','Citroen','2020','Branco',4,170,'Desligado')
CitroenC3.Desligar()
