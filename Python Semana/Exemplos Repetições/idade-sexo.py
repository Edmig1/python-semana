tidade = 0
idadeh = 0
idadem = 0
homem = 0
mulher = 0
for i in range(10):
    sexo = int(input('Digite no Sexo\n1 = Homem - 2 = Mulher \n: '))
    if (sexo == 1):
        homem += 1
        idade= int(input('Digite A idade: '))
        tidade += idade
        idadeh += idade
    elif (sexo == 2):
        idade= int(input('Digite A idade: '))
        mulher += 1
        tidade =+ idade
        idadem =+ idade
print(f'A média da Idade masculina é: {idadeh/homem}')
print(f'A média da Idade feminina é: {idadem/mulher}')
print(f'A média da Idade geral é: {(idadeh+idadem)/(10)}')

