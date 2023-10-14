import customtkinter as tk
import modulo as m
def clique():
    if check1.get() ==1:
        check1.configure(text='marcado')
    else:
        check1.configure(text='marque')
tk.set_appearance_mode('Dark')
janela = m.criarjanela('Opa','300x500',1)
check1 = m.criar_check(janela,'Marque',4,6)
btn = m.criar_btn(janela,'Enviar',clique,200,50,5,6,'red')
janela.mainloop()
