import customtkinter as tk
def clicar():
    n1 = float(input1.get())
    if 2023-(n1) >=18:
        texto1.configure(text='pode tomar birita')
    elif 2023-(n1) <18:
        texto1.configure(text='não pode virar o caneco')
tk.set_appearance_mode('Dark')
janela = tk.CTk()
janela.title('Janelinha daora')
janela.geometry('300x300')
janela.configure(fg_color='#333339')
janela.resizable(width=False, height=False)
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)
texto1 = tk.CTkLabel(janela, text='Coloque o Ano de nascimento', font=("Quicksand"'bold',16),text_color='white')
btn1 = tk.CTkButton(janela, text='Aperte',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= clicar)
input1 = tk.CTkEntry(janela,placeholder_text='Número 2', text_color='white',width=200, height=35, fg_color='transparent',placeholder_text_color='white',border_color='#f5365f')
input1.grid(row=7,column=6)
texto1.grid(row=4,column=6)
btn1.grid(row=8,column=6)
janela.mainloop()