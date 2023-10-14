import customtkinter as tk
from modulo import *
def enviar():
    label2_tela1.configure(text=slider.get())
def tema():
    if switch_tela1.get() ==0:
        tk.set_appearance_mode('Light')
        switch_tela1.configure(text='Tema Claro')
    else:
        tk.set_appearance_mode('Dark')
        switch_tela1.configure(text='Tema Escuro')
tela1= Criar_janela('Login', '600x600+500+0',1)
tk.set_appearance_mode('Light')
tk.set_default_color_theme('themes/green.json')
label1_tela1 = Criar_label(tela1,'Entre em sua conta',3,6)

input1_tela1 = Criar_input(tela1,'Digite Seu Usuário',250,35,4,6)

switch_tela1 = Criar_switch(tela1,'Tema Claro',1,6)
switch_tela1.configure(command=tema)

btn1_tela1 = Criar_btn(tela1,'Enviar Dados',enviar,100,35,5,6)

ListaNomes = ['Coca','Wellington','Mafildo','Enzo','Milim']

combo1_tela1 = Criar_combo(tela1, 250, 35, ListaNomes, 6,6)

label2_tela1 = Criar_label(tela1,'Slider',7,6)
slider = Criar_slider(tela1, 250, 10,8,6)


barra1_tela1 = Criar_barra(tela1, 250, 10,8,6)

img1_tela1 = Criar_imagem(tela1,'joba-bone.jpg',10,6,300,300)

tela1.mainloop()