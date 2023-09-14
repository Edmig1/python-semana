class Cachorro():
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        print('Woof!')
nhoque_charles = Cachorro('Nhoque',7)
nhoque_charles.latir()