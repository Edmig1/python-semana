import customtkinter as tk
def clicar():
    texto1.configure(text=input1.get())
tk.set_appearance_mode('Dark') #Seta a aparencia da janela, pode ser light ou system também
janela = tk.CTk() #declara que essa é a janela principal
janela.title('Janelinha daora') #declara o titulo da janela
janela.geometry('500x500') #Declara o tamanho da janela em pixels
janela.configure(fg_color='#f2f2f2') #muda a cor do background
janela.resizable(width=False, height=False) #trava o tamanho da janela
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)
texto1 = tk.CTkLabel(janela, text='Janelinha daora', font=("Quicksand"'bold',16),text_color='black')
btn1 = tk.CTkButton(janela, text='Aperte',font=("Quicksand"'bold',16),fg_color='#f5365f',hover_color='#b52645',text_color='white', width=100, height=35, command= clicar)
input1 = tk.CTkEntry(janela,placeholder_text='Digita logo fi', text_color='black',width=200, height=35, fg_color='#fcb6c5',placeholder_text_color='#f5365f' )
input1.grid(row=7,column=6)
texto1.grid(row=6,column=6)
btn1.grid(row=8,column=6)
janela.mainloop() #faz com que ela fique na tela, se n usar isso ela brota e some direto