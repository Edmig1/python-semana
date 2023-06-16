nome = ('Godenot', 'Negão', 'Rosa Goiaba', 'Bazonga', 'Lara')
tel = ('123', '456', '789', '156', '286')
email = ('godenot@gmail','negão@gmail','rosagoiaba@gmail','bazonga@gmail','lara@gmail')
print(nome)
esc = int(input('Escolha o número de um contato: '))
esc = esc-1
print('Nome:', nome[esc])
print('Telefone:', tel[esc])
print('Email:', email[esc])
