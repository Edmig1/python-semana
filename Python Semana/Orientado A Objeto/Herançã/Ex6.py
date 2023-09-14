class empregado:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
class gerente:
    def __int__(self,nome,salario,setor):
        self.setor = setor
        super().__int__(nome,salario,setor)