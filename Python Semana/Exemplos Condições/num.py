num = int(input('Digite uma cor: ').lower())
match num:
    case 1:
        print('1')
    case 2:
        print('2')
    case 3:
        print('3')
    case _:
        print('outro')
