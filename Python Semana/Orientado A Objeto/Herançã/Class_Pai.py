class carro:
    def __init__(self, nome, cor, marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca
    def ligar(self):
        print(f'{self.nome} está sendo ligado')
class carro2:
    def __init__(self, ano):
        self.ano = ano
    def farol(self):
        print('Acendendo Faróis')
    def acelerar(self):
        print('Acelerando VRUUUUUUUUUUUUUM')

class carrocitroen(carro, carro2):
    def __init__(self, nome, cor, ano, portas):
        self.portas = portas
        carro.__init__(self,nome, cor,'Citroën')
        carro2.__init__(self,ano)
    def ligar(self):
        print(f'{self.nome} está ligando')

carrocitro = carrocitroen('Cactus','Rosa','2022','4')
print(carrocitro.portas)
carrocitro.ligar()