import customtkinter as tk
nomes = []
precos = []
def add():
    nomes.append((input1.get()))
    precos.append(int(input2.get()))

def exibir():
    valor = max(precos)
    valor = precos.index(valor)
    texto1.configure(text=f'O produto mais caro foi: {nomes[valor]}, custando: {precos[valor]}\n Total: {sum(precos)}')
tk.set_appearance_mode('Dark')
janela = tk.CTk()
janela.title('Janelinha daora')
janela.geometry('500x500')
janela.configure(fg_color='#333339')
janela.resizable(width=False, height=False)
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)
texto1 = tk.CTkLabel(janela, text='calcular notas', font=("Quicksand"'bold',16),text_color='white')
btn1 = tk.CTkButton(janela, text='Aperte',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= add)
btn2 = tk.CTkButton(janela, text='Enviar',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= exibir)
input1 = tk.CTkEntry(janela,placeholder_text='Nome', text_color='white',width=200, height=35, fg_color='transparent',placeholder_text_color='white',border_color='#f5365f')
input2 = tk.CTkEntry(janela,placeholder_text='Preço', text_color='white',width=200, height=35, fg_color='transparent',placeholder_text_color='white',border_color='#f5365f')
input1.grid(row=7,column=6)
input2.grid(row=6,column=6)
texto1.grid(row=4,column=6)
btn1.grid(row=8,column=6)
btn2.grid(row=9,column=6)
janela.mainloop()