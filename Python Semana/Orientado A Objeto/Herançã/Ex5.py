class veiculo():
    def __init__(self,nome,marca):
       self.nome = nome
       self.marca = marca
class carro(veiculo):
    def __init__(self,nome,marca,ano,cor,numportas):
        self.ano = ano
        self.cor = cor
        self.numportas = numportas
        super().__init__(nome,marca)
class moto(veiculo):
    def __init__(self,nome,marca,ano,cor):
        self.ano = ano
        self.cor = cor
        super().__init__(nome,marca)