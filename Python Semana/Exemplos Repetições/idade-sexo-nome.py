idadehV = 0
nomehV = 0
idademV = 0
nomemV = 0
for i in range(2):
    sexo = int(input('Digite no Sexo\n1 = Homem - 2 = Mulher \n: '))
    if (sexo == 1):
        idadeh = int(input('Digite a idade: '))
        nomeh =str(input('Digite o nome: '))
        if(idadeh> idadehV):
            idadehV = idadeh
            nomehV = nomeh
    elif (sexo == 2):
        idadem = int(input('Digite A idade: '))
        nomem = str(input('Digite o nome: '))
        if(idadem> idademV):
            idademV = idadem
            nomemV = nomem
print(f'Homem mais Velho{nomehV, idadehV}')
print(f'Mulher mais Velha{nomemV, idademV}')