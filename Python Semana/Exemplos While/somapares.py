total= 0
vezes = 0
while True:
    num = float(input('Digite o número: '))
    if(num==0):
        break
    if(num%2 == 0):
        total += num

    vezes += 1
print(total)