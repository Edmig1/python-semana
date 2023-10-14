import customtkinter as tk
import modulo as m
valor = 0
def prox():
    global valor
    valor +=0.1
    slider.set(valor)
def antes():
    global valor
    valor -=0.1
    slider.set(valor)
tk.set_appearance_mode('Dark')
janela = m.criarjanela('Opa','300x500',1)
texto = m.criar_label(janela,'Slider',5,6)
slider = m.criar_slider(janela,200,10,6,6)
slider.set(0)
m.criar_btn(janela,'Anterior',antes,200,35,4,6,'red')
m.criar_btn(janela,'Próximo',prox,200,35,5,6,'red')
janela.mainloop()


