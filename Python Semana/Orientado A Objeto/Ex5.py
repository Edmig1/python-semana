class aluno():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def media(self):
        print(f'{(self.n1+self.n2)/2}')
Gustavo = aluno(10,8)
Gustavo.media()