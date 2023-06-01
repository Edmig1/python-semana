lista1 = []
for i in range(1,101):
    if(i%2 == 0):
        print(i)
        lista1.append(i)
print(f'{len(lista1)}, Essa é a quantidade de Números Pares')