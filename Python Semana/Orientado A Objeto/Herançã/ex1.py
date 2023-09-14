class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class aluno(pessoa):
    def __init__(self,matricula, nome,idade):
        self.matricula = matricula
        super().__init__(nome,idade)
estudante = aluno('Matriculado','João','18')
print(f'O nome é:{estudante.nome}\n A idade é: {estudante.idade}\n Está matriculado: {estudante.matricula}')