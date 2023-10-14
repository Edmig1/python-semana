import customtkinter as tk
import modulo as m
def clique():
    if switch1.get() ==1:
        switch1.configure(text='marcado')
    else:
        switch1.configure(text='marque')
tk.set_appearance_mode('Dark')
janela = m.criarjanela('Opa','300x500',1)
switch1 = m.criar_switch(janela,'Marque',4,6)
btn = m.criar_btn(janela,'Enviar',clique,200,50,5,6,'red')
janela.mainloop()
