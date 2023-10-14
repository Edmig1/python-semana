import customtkinter as tk
import modulo as m
def clicar():
    n1 = float(input1.get())
    n2 = float(input2.get())
    if (n1+n2)/2 >=6:
        texto1.configure(text='Aprovado')
    elif (n1+n2)/2 < 6:
        texto1.configure(text='Reprovado')
tk.set_appearance_mode('Dark')
janela = m.criarjanela('Opa','300x500')
texto1 = tk.CTkLabel(janela, text='calcular notas', font=("Quicksand"'bold',16),text_color='white')
btn1 = tk.CTkButton(janela, text='Aperte',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= clicar)
input2 = tk.CTkEntry(janela,placeholder_text='Número 1', text_color='white',width=200, height=35, fg_color='transparent',placeholder_text_color='white',border_color='#f5365f')
input1 = tk.CTkEntry(janela,placeholder_text='Número 1', text_color='white',width=200, height=35, fg_color='transparent',placeholder_text_color='white',border_color='#f5365f')
input1.grid(row=7,column=6)
input2.grid(row=6,column=6)
texto1.grid(row=4,column=6)
btn1.grid(row=8,column=6)
janela.mainloop()