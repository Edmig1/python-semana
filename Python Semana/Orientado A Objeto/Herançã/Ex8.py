class bebida:
    def __init__(self,nome,temp,sabor):
        self.nome = nome
        self.temp = temp
        self.sabor = sabor
class cafe(bebida):
    def __init__(self,nome,temp,sabor,forca):
        self.forca = forca
        super().__init__(nome,temp,sabor)

class suco(bebida):
    def __init__(self,nome,temp,sabor,fruta):
        self.fruta = fruta
        super().__init__(nome,temp,sabor)

class refri(bebida):
    def __init__(self,nome,temp,sabor,gas):
        self.gas = gas
        super().__init__(nome,temp,sabor)