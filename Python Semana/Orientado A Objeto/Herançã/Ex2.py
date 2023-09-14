class animal:
    def __init__(self, nome,som):
        self.nome = nome
        self.som = som
    def fazer_som(self):
        print(f'O {self.nome} {self.som}')
class cachorro(animal):
    def __init__(self, nome,som):
        super().__init__(nome,som)
class gato(animal):
    def __init__(self, nome,som):
        super().__init__(nome,som)
class papagaio(animal):
    def __init__(self, nome,som):
        super().__init__(nome,som)
paraguaio = papagaio('Papagaio', 'Fala')
dog = papagaio('Cachorro', 'Late')
gatinho = papagaio('Gatinho', 'Mia')
paraguaio.fazer_som()
gatinho.fazer_som()
dog.fazer_som()