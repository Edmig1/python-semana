import customtkinter as tk
import modulo as m
lista = ['Bazinga', 'Henri', 'Nicolas','Murilo']
tk.set_appearance_mode('Dark')
janela = m.criarjanela('Opa','300x500',1)
m.criar_combo(janela,200,35,lista,6,6)
janela.mainloop()
