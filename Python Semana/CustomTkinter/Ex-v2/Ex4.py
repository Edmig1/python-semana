import customtkinter as tk
from statistics import mode
lista = []
media = 0
def clicar():
    valor = input1.get()
    lista.append(int(valor))
    print(lista)
def enviar():

    texto1.configure(text=f'A quantidade de termos é: {len(lista)}')


tk.set_appearance_mode('Dark')
janela = tk.CTk()
janela.title('Janelinha daora')
janela.geometry('600x600')
janela.configure(fg_color='#333339')
janela.resizable(width=False, height=False)
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)
texto1 = tk.CTkLabel(janela, text='Digite vários valores', font=("Quicksand"'bold',16),text_color='white')
btn1 = tk.CTkButton(janela, text='Aperte',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= clicar)
btn2 = tk.CTkButton(janela, text='Enviar',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= enviar)
input1 = tk.CTkEntry(janela,placeholder_text='Número 2', text_color='white',width=200, height=35, fg_color='transparent',placeholder_text_color='white',border_color='#f5365f')
input1.grid(row=4,column=5, columnspan=2)
btn1.grid(row=5,column=0,columnspan=12)
btn2.grid(row=6,column=0,columnspan=12)
texto1.grid(row=3,column=0,columnspan=12)
janela.mainloop()