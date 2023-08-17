def voto(id):
    if id <16:
        return 'Voto Negado'
    elif id >15 and id < 18:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatório'
print(voto(17))