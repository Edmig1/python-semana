animal = (input('Digite uma animal: ').lower())
match animal:
    case 'ovelha':
        print('Temos na fazenda')
    case 'vaca':
        print('Temos na fazenda')
    case 'galinhaa':
        print('Temos na fazenda')
    case _:
        print('Não temos')
