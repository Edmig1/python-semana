listac = []
cliente = float(input('Digite A temperatura do Cliente, ou digite 0 para sair: '))
listac.append(cliente)
while(cliente != 0):
    cliente = float(input('Digite A temperatura do Cliente, ou digite 0 para sair: '))
    listac.append(cliente)
    if cliente == 0:
        listac.pop()
for i in(listac):
    total = sum(listac)
print(f'{len(listac)} pessoas fizeram o exame')
print(f'{total/len(listac)} foi a média de temperatura dos Clientes')