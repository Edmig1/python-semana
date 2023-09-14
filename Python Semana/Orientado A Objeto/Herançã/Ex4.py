class produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
class bateria(produto):
    def __init__(self,nome,preco,voltagem):
        self.voltagem = voltagem
        super().__init__(nome,preco)
class oculos(produto):
    def __init__(self,nome,preco,grau):
        self.grau = grau
        super().__init__(nome,preco)
glasses = oculos('óculos','R$ 100','5°')
print(glasses.nome,glasses.preco,glasses.grau)
baterias = bateria('Bateria','R$ 70','100v')
print(baterias.nome,baterias.preco,baterias.voltagem)
