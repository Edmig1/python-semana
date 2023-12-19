class usuario():
    def __init__(self,login,nome,cpf,genero,data,senha):
        self.login = login
        self.nome = nome
        self.cpf = cpf
        self.genero = genero
        self.data = data
        self.senha = senha

usuarios = []

def add_db(login,nome,cpf,genero,data,senha):
    user = usuario(login,nome,cpf,genero,data,senha)
    usuarios.append(user)
def autenticar(login,senha):
    if not usuarios:
        return 'vazia'
    for i in usuarios:
        if i.login == login and i.senha == senha:
            return 'sucesso'
        else:
            return 'falhou'