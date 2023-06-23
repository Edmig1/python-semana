pessoa = {'Nome':'Henri','Idade':16,'Altura':1}
pessoa2 = {'Nome':'Brenda','Peso':60,'Sexo':'F'}
idad = int(input('Digite sua idade:'))
for i,j in pessoa.items():
    print(i+':',j)
if idad == pessoa['Idade']:
    print('Bora tomar uma!')