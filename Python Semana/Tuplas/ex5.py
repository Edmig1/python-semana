nome = ('Doritos', 'Ruffles', 'Cebolitos', 'Fandangos', 'Baconzitos')
preço = ('10,00', '8,50', '7,00', '7,00', '8,00')
estoque = ('73','107','142','91','48')
print(nome)
esc = int(input('Escolha o número de um produto: '))
esc = esc-1
print('Nome:', nome[esc])
print('Preço:','R$'+ preço[esc])
print('Estoque:', estoque[esc])