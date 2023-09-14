class instrumento:
    def __init__(self,nome):
        self.nome = nome
    def tocar(self):
        print(f'O instrumento {self.nome} está tocando')
class piano(instrumento):
    def __init__(self, nome):
        super().__init__(nome)
class violino(instrumento):
    def __init__(self, nome):
        super().__init__(nome)
class flauta(instrumento):
    def __init__(self, nome):
        super().__init__(nome)
little_violino = violino('Violino')
little_violino.tocar()
little_piano = piano('Piano')
little_piano.tocar()
little_flauta = flauta('Flauta')
little_flauta.tocar()