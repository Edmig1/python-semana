Dia = (input('Digite uma Dia: ').lower())
match Dia:
    case ('segunda'|'terça'|'quarta'|'quinta'|'sexta'):
        print(f'{Dia} é dia útil ')
    case ('domingo'|'sábado'):
        print(f'{Dia} é final de semana')
    case _:
        print('Esse dia n existe n parcerin')
